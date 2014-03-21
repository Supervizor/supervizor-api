#!/usr/bin/python
# coding: utf-8

import requests
import urllib

SUPERVIZOR_URL = 'http://supervizor.kpk-rs.si/api/v1/json/'

class SupervizorError(Exception):
    pass

def supervizor(davcna=None, sifra_pu=None, offset=0, limit=10):
    if not (davcna or sifra_pu):
        raise ValueError(u"potrebna je davcna številka (davcna) ali šifra proračunskega uporabnika (sifra_pu)")

    url = SUPERVIZOR_URL
    if sifra_pu:
        try:
            sifra_pu = int(sifra_pu)
        except:
            raise ValueError(u"podana šifra proračunskega uporabnika ni število")
        url += 'institution/%s/' % (sifra_pu,)

    if davcna:
        try:
            davcna = int(davcna)
        except:
            raise ValueError(u"podana davčna številka ni število")
        url += 'company/%s/' % (davcna,)

    getparams = {}
    if offset:
        getparams['offset'] = offset
    if limit != 10:
        getparams['limit'] = limit
    if getparams:
        url = url + '?' + urllib.urlencode(getparams)
    print url
    resp = requests.get(url)
    if resp.status_code != 200:
        print resp.content
        raise SupervizorError()
    data = resp.json()
    return data


if __name__ == "__main__":
    import unittest2

    class SupervizorAPITest(unittest2.TestCase):
        def setUp(self):
            pass
        def runTest(self):
            from pprint import pprint

            data = supervizor(davcna=59093927)
            self.assertEqual('gov_institution' in data, False)
            self.assertEqual('company' in data, True)

            data = supervizor(sifra_pu=13153)
            self.assertEqual('gov_institution' in data, True)
            self.assertEqual('company' in data, False)

            data = supervizor(davcna=59093927, sifra_pu=13153)
            limited_transactions = len(data['transactions'])

            data = supervizor(davcna=59093927, sifra_pu=13153, limit=0)
            all_transactions = len(data['transactions'])
            self.assertEqual(limited_transactions <= all_transactions, True)

    unittest2.main()



