buttons = {}

attributes = {
    'container': '.container',
    'intro_message': '#intro-message',
    'intro_message_text': '#intro-message h2',
    'featured_image': '.carousel-inner',
    'master_plan_section': '.section-master-plan',
    'register_section': '.section-register',
    'register_banner': '.register-banner',
    'register_content': '.section-register-content',
    'featured_article_section': '.featured-article-block',
    'featured_article_image': '.featured-img img',
    'featured_article_title': '.featured-article-title h3',
    'trending_article_section': '.region-trending-article',
    'tonic_promo': '.tonic-promo',
    'tonic_live_video': '.tonic-enhances-lives-video',
    'tonic_live_video_text': '.tonic-enhances-lives-texts-block',
    'stay_connected': '.stay-connected',
    'facebook_link': '.stay-connected a[href="https://www.facebook.com/tonicbd/"]',
    'latest_article_section': '.latest-articles',
    'tonic_doctor_section': '.meet-tonic-doctor',
    'tonic_benefit_section': '.tonic-benefits-section',
    'register_section_secondary': '.section-register-secondary',
}

links = {
    'login': 'a[href="/bn/sign-in"]',
    'register': 'a[href="/bn/join-tonic"]',
    'show_more_latest_articles': '.popular-articles-header a[href="/bn/latest-articles"]',
}

lists = {
    'featured_images': '.carousel-inner .item',
    'trending_articles': '.region-trending-article .trending-article',
    'latest_articles': '.latest-articles .popular-article',
}


CSS_SELECTORS = {
    'buttons': buttons,
    'attributes': attributes,
    'links': links,
    'lists': lists,
}
