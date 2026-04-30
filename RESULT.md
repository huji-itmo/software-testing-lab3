# SPEC.md - Blogger Dashboard HTML Analysis

## Overview
This HTML file represents the **Blogger Admin Dashboard** - the backend interface for managing a Blogger blog called "huji-blog". It is a Google Blogger platform management interface in Russian.

## Page Components Identified

### 1. Header/Navigation Bar
- **Blogger Logo** - Links to Blogger homepage
- **Blog Selector** - Dropdown to switch between blogs (currently showing "huji-blog")
- **Create New Post Button** - Primary action button to create blog posts
- **Blog Menu Links**:
  - Сообщения (Posts)
  - Статистика (Stats)
  - Комментарии (Comments)
  - Прибыль (Earnings)
  - Страницы (Pages)
  - Дизайн (Layout/Design)
  - Тема (Theme)
  - Настройки (Settings)
- **Reading List** - Список чтения
- **View Blog** - Link to public blog (huji42.blogspot.com)
- **Google Account Menu** - User profile access
- **Help Menu** - Справка/отзыв (Help/Feedback)

### 2. Status Filter Dropdown
Options available:
- Все (All) - 1 post
- Опубликованные (Published) - 1 post
- Черновики (Drafts) - 0 posts
- Запланированные (Scheduled) - 0 posts
- Корзина (Trash) - 1 post

### 3. Bulk Action Buttons
- Опубликовать (Publish)
- Переместить в черновики (Move to drafts)
- Применить ярлыки (Apply labels)
- Переместить в корзину (Move to trash)

### 4. Post List
- Single post displayed: "дорогой дневник..." (dear diary...)
- Author: hujij
- Published: 18 апр. 2026 (April 18, 2026)
- 0 comments, 0 views
- Post has checkbox for selection

### 5. Post Action Buttons (per item)
- Поделиться (Share)
- Переместить в черновики (Move to drafts)
- Применить ярлыки (Apply labels)
- Переместить в корзину (Move to trash)
- Посмотреть (View)

### 6. Cookie Notice Banner
EU cookie compliance notice that can be dismissed

### 7. Search Bar
- Located in header for searching content

---

# Selenium Test Ideas (9 Tests)

## Test 1: Verify Page Title and Header Elements
- **Description**: Verify that the Blogger dashboard loads with correct title and all header elements are present
- **Elements to verify**:
  - Blogger logo is displayed and clickable
  - Blog selector shows "huji-blog"
  - "Create new post" button exists
  - All blog menu items are visible (Posts, Stats, Comments, etc.)
- **Expected**: Page loads without errors, all elements present

## Test 2: Test Blog Selector Dropdown Functionality
- **Description**: Verify the blog selector dropdown opens and displays all available blogs
- **Steps**:
  1. Click on blog selector dropdown
  2. Verify dropdown menu appears
  3. Verify "Ваши блоги" (Your blogs) option exists
  4. Verify "Новый блог..." (New blog...) option exists
- **Expected**: Dropdown opens, shows blog options

## Test 3: Test Status Filter Dropdown
- **Description**: Verify post status filter works correctly
- **Steps**:
  1. Click status filter dropdown
  2. Verify all options: All, Published, Drafts, Scheduled, Trash
  3. Select each option and verify displayed count changes
- **Expected**: Filter updates post list based on selection

## Test 4: Test Create New Post Button
- **Description**: Verify the "Create new post" button is clickable and navigates to post editor
- **Steps**:
  1. Click "Написать" (Write) button in header
  2. Verify navigation or modal opens
  3. Or click the floating action button
- **Expected**: Button triggers post creation flow

## Test 5: Test Post Selection and Bulk Actions
- **Description**: Verify checkbox selection and bulk action buttons work
- **Steps**:
  1. Click checkbox on a post
  2. Verify "0 из 1" counter updates to "1 из 1"
  3. Verify bulk action buttons become active
  4. Test "Move to trash" action
- **Expected**: Selection works, bulk actions enabled

## Test 6: Test Individual Post Actions
- **Description**: Verify post row action buttons function correctly
- **Steps**:
  1. Hover over the post to reveal action buttons
  2. Test "View" (Посмотреть) - should open blog post in new tab
  3. Test "Move to drafts" action
  4. Test "Move to trash" action
- **Expected**: Each action functions properly

## Test 7: Test Navigation Menu Links
- **Description**: Verify all blog management menu links
- **Steps**:
  1. Hover over blog menu to reveal all links
  2. Click each menu item:
     - Posts (Сообщения) - /blog/posts/
     - Stats (Статистика) - /blog/stats/
     - Comments (Комментарии) - /blog/comments/
     - Pages (Страницы) - /blog/pages/
     - Layout (Дизайн) - /blog/layout/
     - Theme (Тема) - /blog/themes/
     - Settings (Настройки) - /blog/settings/
- **Expected**: All links navigate to correct pages

## Test 8: Test Cookie Notice Dismissal
- **Description**: Verify EU cookie notice can be dismissed
- **Steps**:
  1. Verify cookie notice banner is visible
  2. Click dismiss/close button (X icon)
  3. Verify notice disappears
- **Expected**: Notice dismissed, stays hidden on reload

## Test 9: Test View Blog Link
- **Description**: Verify external blog link opens public blog
- **Steps**:
  1. Click "Посмотреть блог" (View blog) button
  2. Verify new tab opens with URL huji42.blogspot.com
- **Expected**: External blog opens correctly

---

# Additional Considerations

## Locator Strategies for Selenium
- Use **aria-label** attributes for button identification (most reliable)
- Use **jsname** attributes for programmatic element identification
- Use **data-value** for dropdown options
- CSS classes like `.U26fgb` for button elements

## Async Considerations
- Page uses AngularJS (c-wiz components)
- Elements may load asynchronously - use explicit waits
- jsmodel attributes indicate deferred loading

## Test Data
- Blog ID: 6104660592042377337
- Post ID: 598533632361174129
- Logged in user: mczhelt0k@gmail.com

---

# Summary

This HTML represents a fully-featured Blogger admin dashboard. The 9 test ideas cover:
1. Page load validation
2. Blog switching functionality
3. Post filtering
4. Post creation entry point
5. Bulk operations
6. Individual post operations
7. Navigation throughout the dashboard
8. Cookie consent UI
9. External blog preview

These tests verify the core functionality a user would interact with when managing their Blogger blog.