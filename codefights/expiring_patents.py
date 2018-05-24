from sgk_test import test
import re
import urllib.request
import json
from datetime import datetime

"""
Required Request Header:
Content-Type:application/json;charset=utf-8
"""

"""
{"searchText":"XXXXXX" ,"qf":"appEarlyPubNumber applId appLocation appType appStatus_txt appConfrNumber appCustNumber \
appGrpArtNumber appCls appSubCls appEntityStatus_txt patentNumber patentTitle primaryInventor firstNamedApplicant \
appExamName appExamPrefrdName appAttrDockNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber pctAppType \
firstInventorFile appClsSubCls rankAndInventorsList","facet":"true","sort":"applId asc","start":"0"}
"""


# def expiringPatents_PRACTICE(patents):
def expiringPatents(patents):
    return

def expiringPatents_PASSED(patents):
# def expiringPatents(patents):
    def query(param):
        """
        If it starts with "US" it's a patent number (query without the US)
        If it's a plain number, it's an application number
        """
        if param.startswith("US "):
            payload = bytes("{\"searchText\":\"patentNumber:(" + param[3:] + ")\", \"qf\":\"appEarlyPubNumber applId \
            appLocation appType appStatus_txt appConfrNumber appCustNumber appGrpArtNumber appCls appSubCls \
            appEntityStatus_txt patentNumber patentTitle primaryInventor firstNamedApplicant appExamName \
            appExamPrefrdName appAttrDockNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber pctAppType \
            firstInventorFile appClsSubCls rankAndInventorsList\"}","utf-8")
        else:
            payload = bytes(
                "{\"searchText\":\"applId:(" + param + ")\", \"qf\":\"appEarlyPubNumber applId appLocation appType \
                appStatus_txt appConfrNumber appCustNumber appGrpArtNumber appCls appSubCls appEntityStatus_txt \
                patentNumber patentTitle primaryInventor firstNamedApplicant appExamName appExamPrefrdName \
                appAttrDockNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber pctAppType firstInventorFile \
                appClsSubCls rankAndInventorsList\"}",
                "utf-8")

        req = urllib.request.Request("https://ped.uspto.gov/api/queries")
        req.add_header('Content-Type', 'application/json;charset=utf-8')
        resp = urllib.request.urlopen(req, payload)
        content = resp.read()
        data = json.loads(content.decode("utf-8"))
        query_results = data.get("queryResults")
        search_response = query_results.get("searchResponse")
        response = search_response.get("response")
        docs = response.get("docs")[0]
        app_filing_date = docs.get("appFilingDate")

        return app_filing_date

    ret_year = ret_month = ret_day = 0
    retval = ""
    for elem in patents:
        date = query(elem)
        idx = date.index("T")
        date = date[:idx]
        lst = date.split("-")
        year = int(lst[0])
        month = int(lst[1])
        day = int(lst[2])
        if year == ret_year:
            if month > ret_month:
                ret_year = year
                ret_month = month
                ret_day = day
                retval = date
            elif month == ret_month:
                if day > ret_day:
                    ret_year = year
                    ret_month = month
                    ret_day = day
                    retval = date

        elif year > ret_year:
            ret_year = year
            ret_month = month
            ret_day = day
            retval = date

    retval = str(ret_year+20) + retval[4:]
    return retval






def main():
    ######### TESTS ############
    test("2023-02-12", expiringPatents(["60447158"]))
    test("2024-03-31", expiringPatents(["US 4233942", "10816446", "US 6932365"]))
    test("2027-04-25", expiringPatents(["US 7051371", "US 6929164", "US 8051371"]))



if __name__ == "__main__":
    main()

