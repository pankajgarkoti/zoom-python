# AccountsaccountIdsettingsOtherOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_active_users** | **bool** | If true, administrators can activate users with a single default passcode when adding users. This activates added users immediately without waiting for them to set their own passcode. | [optional] 
**allow_users_contact_support_via_chat** | **bool** | If true, displays the Zoom Help badge on the bottom-right of the page. | [optional] 
**allow_users_enter_and_share_pronouns** | **bool** | If true, users can add pronouns to their profile cards and share them during meetings and webinars. | [optional] 
**blur_snapshot** | **bool** | If true, iOS blurs the screenshot in the task switcher when multiple apps are open. Android hides the screenshot in the system-level list of recent apps. | [optional] 
**display_meetings_scheduled_for_others** | **bool** | If true, a user with [scheduling privileges](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-privilege) can view other users&#x27; meetings. | [optional] 
**meeting_qos_and_mos** | **int** | The dashboard meeting [quality scores and network alerts](https://support.zoom.us/hc/en-us/articles/360061244651) setting.  * &#x60;0&#x60; - Do not enable meeting quality scores and network alerts on the dashboard.  * &#x60;1&#x60; - Display the meeting quality score and network alerts on the dashboard.  * &#x60;2&#x60; - Use custom thresholds for quality scores and network alerts. * &#x60;3&#x60; - Display the meeting quality score and network alerts on the dashboard and use custom thresholds for quality scores and network alerts. | [optional] 
**show_one_user_meeting_on_dashboard** | **bool** | If true, meetings with only one person will display on the dashboard and in reports. | [optional] 
**use_cdn** | **str** | Allow connections to different CDNs (content delivery networks) for a better web browsing experience. All users in your organization will use the selected CDN to access static resources.  * &#x60;none&#x60; - Do not use a CDN.  * &#x60;default&#x60; - Use the Amazon CloudFront CDN for users **except** Chinese Mainland users. Chinese Mainland users will use the Wangsu CDN (China).  * &#x60;wangsu&#x60; - Use the Wangsu CDN for all users. | [optional] 
**webinar_registration_options** | [**AccountsaccountIdsettingsOtherOptionsWebinarRegistrationOptions**](AccountsaccountIdsettingsOtherOptionsWebinarRegistrationOptions.md) |  | [optional] 
**email_in_attendee_report_for_meeting** | **bool** | If true, include authenticated guests&#x27; email addresses in attendee reports for meetings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

