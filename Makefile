.PHONY: test test-theme-toggle test-font-size-decrease test-font-size-increase test-card-view-toggle test-feed-tabs-popular test-feed-tabs-story test-tag-button test-search-input test-load-new-articles test-logo-click test-switchnonegative

test:
	python -m pytest tests/ -v

test-theme-toggle:
	python -m pytest tests/test_theme_toggle.py -v

test-font-size-decrease:
	python -m pytest tests/test_font_size_decrease.py -v

test-font-size-increase:
	python -m pytest tests/test_font_size_increase.py -v

test-card-view-toggle:
	python -m pytest tests/test_card_view_toggle.py -v

test-feed-tabs-popular:
	python -m pytest tests/test_feed_tabs_popular.py -v

test-feed-tabs-story:
	python -m pytest tests/test_feed_tabs_story.py -v

test-tag-button:
	python -m pytest tests/test_tag_button.py -v

test-search-input:
	python -m pytest tests/test_search_input.py -v

test-load-new-articles:
	python -m pytest tests/test_load_new_articles.py -v

test-logo-click:
	python -m pytest tests/test_logo_click.py -v

test-switchnonegative:
	python -m pytest tests/test_switchnonegative.py -v