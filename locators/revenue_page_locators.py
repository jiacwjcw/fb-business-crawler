from selenium.webdriver.common.by import By


class RevenuePageLocators:

    # Common
    DATE_SELECTOR_BUTTON = (
        By.XPATH, "/html[@id='facebook']//div[@id='bizsitePageContainer']/div[@id='globalContainer']/div[1]/div[@id='power_editor_root']/div[@id='ads_pe_container']//span/span/button"
    )
    DATE_SELECTOR_DEFAULT_EARLIEST_OPTION = (
        By.XPATH, "/html[@id='facebook']//div[@id='bizsitePageContainer']/div[@id='globalContainer']//ul[@aria-label='日期範圍選擇功能表']/li[@data-hover='tooltip'][2]"
    )

    # First Section
    AD_MARKETING_ITEM = (
        By.XPATH, "/html[@id='facebook']//div[@id='bizsitePageContainer']/div[@id='globalContainer']/div/div[@id='power_editor_root']/div[@id='ads_pe_container']//div[@data-hover='tooltip']/a/span"
    )

    # Second Sction
    ADS_RAW = (
        By.XPATH, "/html[@id='facebook']//div[@id='bizsitePageContainer']/div[@id='globalContainer']/div[1]/div[@id='power_editor_root']/div[@id='ads_pe_container']//div[@role='table']//div[@class='_219p']/div[@class='_1gda _2djg']"
    )
    AD_FIELDS = (
        By.XPATH, ".//div[contains(@class, '_4lg0') and contains(@class, '_4h2m')]"
    )

    AD_FIELD_SPAN = (
        By.XPATH, ".//span"
    )
