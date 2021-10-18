import logging
from utils.helper import *
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.revenue_page_locators import RevenuePageLocators
from utils.ad_field_type_helper import AdFieldTypeHelper


class RevenuePage(BasePage):

    revenue_locators = RevenuePageLocators

    def click_Q3_marketing(self):
        logging.info("Click Q3 marketing target")
        self.find_element(self.revenue_locators.AD_MARKETING_ITEM).click()

    def set_default_date_to_earliest_option(self):
        self.find_element(self.revenue_locators.DATE_SELECTOR_BUTTON).click()
        self.find_element(
            self.revenue_locators.DATE_SELECTOR_DEFAULT_EARLIEST_OPTION).click()
        self.wait_page_until_loading()
        if "最早" in self.find_element(self.revenue_locators.DATE_SELECTOR_BUTTON).text:
            logging.info("Set default date to 最早")

    def _get_ads(self):
        _elements = self.find_elements(self.revenue_locators.ADS_RAW)
        return _elements

    def _get_ad_fields(self, ad_element):
        return ad_element.find_elements(
            self.revenue_locators.AD_FIELDS[0], self.revenue_locators.AD_FIELDS[1]
        )

    def _get_field_span_value(self, field_element):
        return field_element.find_element(
            self.revenue_locators.AD_FIELD_SPAN[0], self.revenue_locators.AD_FIELD_SPAN[1]
        ).text

    def _get_all_ad_info(self):
        ads_info_list = list()
        ads = self._get_ads()
        for ad in ads:
            fields = self._get_ad_fields(ad)

            ad_name = self._get_field_span_value(
                fields[AdFieldTypeHelper().AD_NAME])
            ad_status = self._get_field_span_value(
                fields[AdFieldTypeHelper().AD_STATUS])
            ad_cost = self._get_field_span_value(
                fields[AdFieldTypeHelper().AD_COST])
            ad_schedule = self._get_field_span_value(
                fields[AdFieldTypeHelper().AD_SCHEDULE])
            ad_end_time = self._get_field_span_value(
                fields[AdFieldTypeHelper().AD_END_TIME])

            ads_info_list.append({
                "ad_name": ad_name,
                "ad_status": ad_status,
                "ad_cost": ad_cost,
                "ad_start_time": get_start_time_from_schedule(ad_schedule),
                "ad_end_time": get_regex_time(ad_end_time)
            })

        return ads_info_list

    def get_ads_cost(self):
        ads_info_list = self._get_all_ad_info()
        new_list = list()
        while ads_info_list:
            left = 0
            right = len(ads_info_list)-1
            pivot = get_regex_ad_name(ads_info_list[left]["ad_name"])
            cost = get_regex_ad_cost(ads_info_list[left]["ad_cost"])

            while right > left:
                if get_regex_ad_name(ads_info_list[right]["ad_name"]) == pivot:
                    cost += get_regex_ad_cost(ads_info_list[right]["ad_cost"])
                    ads_info_list.pop(right)
                right -= 1

            new_list.append({
                "ad_name": pivot,
                "ad_cost": cost,
                "ad_start_time": ads_info_list[left]["ad_start_time"]
            })

            ads_info_list.pop(left)

        return new_list
