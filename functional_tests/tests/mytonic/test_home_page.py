# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nose.plugins.attrib import attr

from config.config import MY_TONIC_DOMAIN
from functional_tests.css_selectors import CSS_SELECTORS
from functional_tests.tests.base.base import FunctionalTest


@attr('website')
class TestTonicHomePage(FunctionalTest):
    home_url = MY_TONIC_DOMAIN

    def test_home_page(self):
        self.driver.get(self.home_url)
        self.driver_api.waits.wait_till_element_is_visible(CSS_SELECTORS['attributes']['container'])

        print 'Verifying login link and text...'
        login_text = self.driver.find_element_by_css_selector(
            CSS_SELECTORS['links']['login']).text
        assert login_text == 'লগ ইন', 'Login link text doesn\'t match'

        print 'Verifying register link and text...'
        register_text = self.driver.find_element_by_css_selector(
            CSS_SELECTORS['links']['register']).text
        assert register_text == 'রেজিস্টার', 'Register link text doesn\'t match'

        print 'Verifying introduction message...'
        intro_err_msg = 'Intro message missing in home page'
        assert self.driver_api.is_element_visible(CSS_SELECTORS['attributes']['intro_message']), intro_err_msg

        print 'Verifying featured image...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['featured_image']), 'Featured image missing'

        featured_images = self.driver.find_elements_by_css_selector(CSS_SELECTORS['lists']['featured_images'])
        assert len(featured_images) == 5, 'There are {} featured images instead of 5'.format(str(len(featured_images)))

        print 'Verifying master plan section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['master_plan_section']), 'Master plan section missing'

        print 'Verifying register section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['register_section']), 'Register section missing'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['register_banner']), 'Register banner missing'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['register_content']), 'Register content missing'

        print 'Verifying featured article section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['featured_article_section']), 'Featured article missing'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['featured_article_image']), 'Missing featured article image'

        featured_article_title = self.driver.find_element_by_css_selector(
            CSS_SELECTORS['attributes']['featured_article_title']).text
        assert len(featured_article_title) > 0, 'Featured article title is empty'

        print 'Verifying trending article section...'
        assert self.driver_api.is_element_visible(CSS_SELECTORS['attributes']['trending_article_section'])

        trending_articles = self.driver.find_elements_by_css_selector(CSS_SELECTORS['lists']['trending_articles'])
        assert len(trending_articles) == 3, 'There are {} trending articles instead of 3'.format(
            str(len(trending_articles)))

        print 'Verifying tonic promo...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['tonic_promo']), 'Tonic promo section missing'

        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['stay_connected']), 'Stay connected section missing'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['facebook_link']), 'Facebook link missing in stay connected section'

        print 'Verifying latest article section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['latest_article_section']), 'Latest article section missing'
        latest_articles = self.driver.find_elements_by_css_selector(CSS_SELECTORS['lists']['latest_articles'])

        assert len(latest_articles) == 3, 'There are {} articles instead of 3'.format(str(len(latest_articles)))
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['links']['show_more_latest_articles']), 'Show more latest articles link missing'

        print 'Verifying tonic doctor section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['tonic_doctor_section']), 'Tonic doctor section missing'

        print 'Verifying tonic benefit section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['tonic_benefit_section']), 'Tonic benefit section missing'

        print 'Verifying secondary register section...'
        assert self.driver_api.is_element_visible(
            CSS_SELECTORS['attributes']['register_section_secondary']), 'Secondary register section missing'
