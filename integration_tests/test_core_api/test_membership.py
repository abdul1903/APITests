import random
from unittest import TestCase

from nose.plugins.attrib import attr

from integration_tests.common.member import get_member, get_members


@attr('core', 'member')
class MembershipApiTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        pass

    def test_member_exists(self):
        msisdn = '8801708142984'
        print 'Getting member info for {}'.format(msisdn)
        status_code, res_data = get_member(msisdn)

        print 'validating...'
        assert status_code == 200, 'Status code {} instead of 200 and error text: {}'.format(
            status_code, res_data['message'])
        assert res_data['data']['status'] != 'Cancelled'

    def test_get_members_by_type(self):
        membership_types = ['TonicBasic', 'TonicAdvanced', 'TonicPremium']

        print 'validating membership types...'
        for membership_type in membership_types:
            status_code, res_data = get_members(membership_type=membership_type)

            members = res_data['data']
            length = len(members)
            random_numbers = random.sample(range(1, length), 3)

            for number in random_numbers:
                assert members[number]['membership_type'] == membership_type

            assert status_code == 200, 'Status code {} instead of 200 and error text: {}'.format(
                status_code, res_data['message'])

    def test_get_members_by_status(self):
        member_status = ['Subscribed', 'FullMember', 'Cancelled', 'Suspended']

        print 'validating member status...'
        for status in member_status:
            status_code, res_data = get_members(status=status)

            members = res_data['data']
            length = len(members)
            random_numbers = random.sample(range(1, length), 3)

            for number in random_numbers:
                assert members[number]['status'] == status

            assert status_code == 200, 'Status code {} instead of 200 and error text: {}'.format(
                status_code, res_data['message'])
