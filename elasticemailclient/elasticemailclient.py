import requests
import json
from enum import Enum

from api_types import ApiTypes


class ApiClient:
    apiUri = 'https://api.elasticemail.com/v2'
    apiKey = '00000000-0000-0000-0000-0000000000000'

    def Request(method, url, data=dict(), attachs=None):
        data['apikey'] = ApiClient.apiKey
        if method == 'POST':
            result = requests.post(
                ApiClient.apiUri + url, params=data, files=attachs)
        elif method == 'PUT':
            result = requests.put(ApiClient.apiUri + url, params=data)
        elif method == 'GET':
            attach = ''
            params = {k: v for k, v in data.items() if v is not None}
            result = requests.get(ApiClient.apiUri + url, params=params)

        jsonMy = result.json()

        if jsonMy['success'] is False:
            return jsonMy['error']

        if 'data' in jsonMy.keys():
            return jsonMy['data']
        else:
            return 'success'


""" 
Methods for managing your account and subaccounts.
"""


class Account:

    def AddSubAccount(email, password, confirmPassword, requiresEmailCredits=False, enableLitmusTest=False, requiresLitmusCredits=False, maxContacts=0, enablePrivateIPRequest=True, sendActivation=False, returnUrl=None, sendingPermission=None, enableContactFeatures=None, poolName=None, emailSizeLimit=10, dailySendLimit=None):
        """
        Create new subaccount and provide most important data about it.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string password - Current password.
            string confirmPassword - Repeat new password.
            bool requiresEmailCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            bool enableLitmusTest - True, if account is able to send template tests to Litmus. Otherwise, false (default False)
            bool requiresLitmusCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the account can have (default 0)
            bool enablePrivateIPRequest - True, if account can request for private IP on its own. Otherwise, false (default True)
            bool sendActivation - True, if you want to send activation email to this account. Otherwise, false (default False)
            string returnUrl - URL to navigate to after account creation (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for account (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string poolName - Private IP required. Name of the custom IP Pool which Sub Account should use to send its emails. Leave empty for the default one or if no Private IPs have been bought (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            int? dailySendLimit - Amount of emails account can send daily (default None)
        Returns string
        """
        return ApiClient.Request('GET', '/account/addsubaccount', {
            'email': email,
            'password': password,
            'confirmPassword': confirmPassword,
            'requiresEmailCredits': requiresEmailCredits,
            'enableLitmusTest': enableLitmusTest,
            'requiresLitmusCredits': requiresLitmusCredits,
            'maxContacts': maxContacts,
            'enablePrivateIPRequest': enablePrivateIPRequest,
            'sendActivation': sendActivation,
            'returnUrl': returnUrl,
            'sendingPermission': sendingPermission,
            'enableContactFeatures': enableContactFeatures,
            'poolName': poolName,
            'emailSizeLimit': emailSizeLimit,
            'dailySendLimit': dailySendLimit})

    def AddSubAccountCredits(credits, notes, creditType=ApiTypes.CreditType.Email, subAccountEmail=None, publicAccountID=None):
        """
        Add email, template or litmus credits to a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int credits - Amount of credits to add
            string notes - Specific notes about the transaction
            ApiTypes.CreditType creditType - Type of credits to add (Email or Litmus) (default ApiTypes.CreditType.Email)
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to add credits to. Use subAccountEmail or publicAccountID not both. (default None)
        """
        return ApiClient.Request('GET', '/account/addsubaccountcredits', {
            'credits': credits,
            'notes': notes,
            'creditType': creditType.value,
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID})

    def ChangeEmail(newEmail, confirmEmail, sourceUrl="https://elasticemail.com/account/"):
        """
        Change your email address. Remember, that your email address is used as login!
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string newEmail - New email address.
            string confirmEmail - New email address.
            string sourceUrl - URL from which request was sent. (default "https://elasticemail.com/account/")
        Returns string
        """
        return ApiClient.Request('GET', '/account/changeemail', {
            'newEmail': newEmail,
            'confirmEmail': confirmEmail,
            'sourceUrl': sourceUrl})

    def ChangePassword(currentPassword, newPassword, confirmPassword):
        """
        Create new password for your account. Password needs to be at least 6 characters long.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string currentPassword - Current password.
            string newPassword - New password for account.
            string confirmPassword - Repeat new password.
        """
        return ApiClient.Request('GET', '/account/changepassword', {
            'currentPassword': currentPassword,
            'newPassword': newPassword,
            'confirmPassword': confirmPassword})

    def DeleteSubAccount(notify=True, subAccountEmail=None, publicAccountID=None, deleteDomains=True):
        """
        Deletes specified Subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool notify - True, if you want to send an email notification. Otherwise, false (default True)
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to delete. Use subAccountEmail or publicAccountID not both. (default None)
            bool deleteDomains -  (default True)
        """
        return ApiClient.Request('GET', '/account/deletesubaccount', {
            'notify': notify,
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID,
            'deleteDomains': deleteDomains})

    def GetSubAccountApiKey(subAccountEmail=None, publicAccountID=None):
        """
        Returns API Key for the given Sub Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to retrieve sub-account API Key. Use subAccountEmail or publicAccountID not both. (default None)
        Returns string
        """
        return ApiClient.Request('GET', '/account/getsubaccountapikey', {
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID})

    def GetSubAccountList():
        """
        Lists all of your subaccounts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.SubAccount>
        """
        return ApiClient.Request('GET', '/account/getsubaccountlist')

    def Load():
        """
        Loads your account. Returns detailed information about your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Account
        """
        return ApiClient.Request('GET', '/account/load')

    def LoadAdvancedOptions():
        """
        Load advanced options of your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.AdvancedOptions
        """
        return ApiClient.Request('GET', '/account/loadadvancedoptions')

    def LoadEmailCreditsHistory():
        """
        Lists email credits history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.EmailCredits>
        """
        return ApiClient.Request('GET', '/account/loademailcreditshistory')

    def LoadLitmusCreditsHistory():
        """
        Lists litmus credits history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.LitmusCredits>
        """
        return ApiClient.Request('GET', '/account/loadlitmuscreditshistory')

    def LoadNotificationQueue():
        """
        Shows queue of newest notifications - very useful when you want to check what happened with mails that were not received.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.NotificationQueue>
        """
        return ApiClient.Request('GET', '/account/loadnotificationqueue')

    def LoadPaymentHistory(limit, offset, fromDate, toDate):
        """
        Lists all payments
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items.
            int offset - How many items should be loaded ahead.
            DateTime fromDate - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime toDate - Ending date for search in YYYY-MM-DDThh:mm:ss format.
        Returns List<ApiTypes.Payment>
        """
        return ApiClient.Request('GET', '/account/loadpaymenthistory', {
            'limit': limit,
            'offset': offset,
            'fromDate': fromDate,
            'toDate': toDate})

    def LoadPayoutHistory():
        """
        Lists all referral payout history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Payment>
        """
        return ApiClient.Request('GET', '/account/loadpayouthistory')

    def LoadReferralDetails():
        """
        Shows information about your referral details
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Referral
        """
        return ApiClient.Request('GET', '/account/loadreferraldetails')

    def LoadReputationHistory(limit=20, offset=0):
        """
        Shows latest changes in your sending reputation
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.ReputationHistory>
        """
        return ApiClient.Request('GET', '/account/loadreputationhistory', {
            'limit': limit,
            'offset': offset})

    def LoadReputationImpact():
        """
        Shows detailed information about your actual reputation score
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.ReputationDetail
        """
        return ApiClient.Request('GET', '/account/loadreputationimpact')

    def LoadSpamCheck(limit=20, offset=0):
        """
        Returns detailed spam check.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.SpamCheck>
        """
        return ApiClient.Request('GET', '/account/loadspamcheck', {
            'limit': limit,
            'offset': offset})

    def LoadSubAccountsEmailCreditsHistory(subAccountEmail=None, publicAccountID=None):
        """
        Lists email credits history for sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to list history for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns List<ApiTypes.EmailCredits>
        """
        return ApiClient.Request('GET', '/account/loadsubaccountsemailcreditshistory', {
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID})

    def LoadSubAccountSettings(subAccountEmail=None, publicAccountID=None):
        """
        Loads settings of subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to load settings for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns ApiTypes.SubAccountSettings
        """
        return ApiClient.Request('GET', '/account/loadsubaccountsettings', {
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID})

    def LoadSubAccountsLitmusCreditsHistory(subAccountEmail=None, publicAccountID=None):
        """
        Lists litmus credits history for sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to list history for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns List<ApiTypes.LitmusCredits>
        """
        return ApiClient.Request('GET', '/account/loadsubaccountslitmuscreditshistory', {
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID})

    def LoadUsage(EEfrom, to):
        """
        Shows usage of your account in given time.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
        Returns List<ApiTypes.Usage>
        """
        return ApiClient.Request('GET', '/account/loadusage', {
            'from': EEfrom,
            'to': to})

    def ManageApiKeys(apiKey, action):
        """
        Manages your apikeys.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string apiKey - APIKey you would like to manage.
            ApiTypes.APIKeyAction action - Specific action you would like to perform on the APIKey
        Returns List<string>
        """
        return ApiClient.Request('GET', '/account/manageapikeys', {
            'apiKey': apiKey,
            'action': action.value})

    def Overview():
        """
        Shows summary for your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.AccountOverview
        """
        return ApiClient.Request('GET', '/account/overview')

    def ProfileOverview():
        """
        Shows you account's profile basic overview
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Profile
        """
        return ApiClient.Request('GET', '/account/profileoverview')

    def RemoveSubAccountCredits(creditType, notes, subAccountEmail=None, publicAccountID=None, credits=None, removeAll=False):
        """
        Remove email, template or litmus credits from a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.CreditType creditType - Type of credits to add (Email or Litmus)
            string notes - Specific notes about the transaction
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to remove credits from. Use subAccountEmail or publicAccountID not both. (default None)
            int? credits - Amount of credits to remove (default None)
            bool removeAll - Remove all credits of this type from sub-account (overrides credits if provided) (default False)
        """
        return ApiClient.Request('GET', '/account/removesubaccountcredits', {
            'creditType': creditType.value,
            'notes': notes,
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID,
            'credits': credits,
            'removeAll': removeAll})

    def RequestPremiumSupport():
        """
        Request premium support for your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        """
        return ApiClient.Request('GET', '/account/requestpremiumsupport')

    def RequestPrivateIP(count, notes):
        """
        Request a private IP for your Account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int count - Number of items.
            string notes - Free form field of notes
        """
        return ApiClient.Request('GET', '/account/requestprivateip', {
            'count': count,
            'notes': notes})

    def UpdateAdvancedOptions(enableClickTracking=None, enableLinkClickTracking=None, manageSubscriptions=None, manageSubscribedOnly=None, transactionalOnUnsubscribe=None, skipListUnsubscribe=None, autoTextFromHtml=None, allowCustomHeaders=None, bccEmail=None, contentTransferEncoding=None, emailNotificationForError=None, emailNotificationEmail=None, webNotificationUrl=None, webNotificationNotifyOncePerEmail=None, webNotificationForSent=None, webNotificationForOpened=None, webNotificationForClicked=None, webNotificationForUnsubscribed=None, webNotificationForAbuseReport=None, webNotificationForError=None, hubCallBackUrl="", inboundDomain=None, inboundContactsOnly=None, lowCreditNotification=None, enableUITooltips=None, enableContactFeatures=None, notificationsEmails=None, unsubscribeNotificationsEmails=None, logoUrl=None, enableTemplateScripting=True, staleContactScore=None, staleContactInactiveDays=None, deliveryReason=None, tutorialsEnabled=None):
        """
        Update sending and tracking options of your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool? enableClickTracking - True, if you want to track clicks. Otherwise, false (default None)
            bool? enableLinkClickTracking - True, if you want to track by link tracking. Otherwise, false (default None)
            bool? manageSubscriptions - True, if you want to display your labels on your unsubscribe form. Otherwise, false (default None)
            bool? manageSubscribedOnly - True, if you want to only display labels that the contact is subscribed to on your unsubscribe form. Otherwise, false (default None)
            bool? transactionalOnUnsubscribe - True, if you want to display an option for the contact to opt into transactional email only on your unsubscribe form. Otherwise, false (default None)
            bool? skipListUnsubscribe - True, if you do not want to use list-unsubscribe headers. Otherwise, false (default None)
            bool? autoTextFromHtml - True, if text BODY of message should be created automatically. Otherwise, false (default None)
            bool? allowCustomHeaders - True, if you want to apply custom headers to your emails. Otherwise, false (default None)
            string bccEmail - Email address to send a copy of all email to. (default None)
            string contentTransferEncoding - Type of content encoding (default None)
            bool? emailNotificationForError - True, if you want bounce notifications returned. Otherwise, false (default None)
            string emailNotificationEmail - Specific email address to send bounce email notifications to. (default None)
            string webNotificationUrl - URL address to receive web notifications to parse and process. (default None)
            bool? webNotificationNotifyOncePerEmail - True, if you want to receive notifications for each type only once per email. Otherwise, false (default None)
            bool? webNotificationForSent - True, if you want to send web notifications for sent email. Otherwise, false (default None)
            bool? webNotificationForOpened - True, if you want to send web notifications for opened email. Otherwise, false (default None)
            bool? webNotificationForClicked - True, if you want to send web notifications for clicked email. Otherwise, false (default None)
            bool? webNotificationForUnsubscribed - True, if you want to send web notifications for unsubscribed email. Otherwise, false (default None)
            bool? webNotificationForAbuseReport - True, if you want to send web notifications for complaint email. Otherwise, false (default None)
            bool? webNotificationForError - True, if you want to send web notifications for bounced email. Otherwise, false (default None)
            string hubCallBackUrl - URL used for tracking action of inbound emails (default "")
            string inboundDomain - Domain you use as your inbound domain (default None)
            bool? inboundContactsOnly - True, if you want inbound email to only process contacts from your account. Otherwise, false (default None)
            bool? lowCreditNotification - True, if you want to receive low credit email notifications. Otherwise, false (default None)
            bool? enableUITooltips - True, if account has tooltips active. Otherwise, false (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string notificationsEmails - Email addresses to send a copy of all notifications from our system. Separated by semicolon (default None)
            string unsubscribeNotificationsEmails - Emails, separated by semicolon, to which the notification about contact unsubscribing should be sent to (default None)
            string logoUrl - URL to your logo image. (default None)
            bool? enableTemplateScripting - True, if you want to use template scripting in your emails {{}}. Otherwise, false (default True)
            int? staleContactScore - (0 means this functionality is NOT enabled) Score, depending on the number of times you have sent to a recipient, at which the given recipient should be moved to the Stale status (default None)
            int? staleContactInactiveDays - (0 means this functionality is NOT enabled) Number of days of inactivity for a contact after which the given recipient should be moved to the Stale status (default None)
            string deliveryReason - Why your clients are receiving your emails. (default None)
            bool? tutorialsEnabled -  (default None)
        Returns ApiTypes.AdvancedOptions
        """
        return ApiClient.Request('GET', '/account/updateadvancedoptions', {
            'enableClickTracking': enableClickTracking,
            'enableLinkClickTracking': enableLinkClickTracking,
            'manageSubscriptions': manageSubscriptions,
            'manageSubscribedOnly': manageSubscribedOnly,
            'transactionalOnUnsubscribe': transactionalOnUnsubscribe,
            'skipListUnsubscribe': skipListUnsubscribe,
            'autoTextFromHtml': autoTextFromHtml,
            'allowCustomHeaders': allowCustomHeaders,
            'bccEmail': bccEmail,
            'contentTransferEncoding': contentTransferEncoding,
            'emailNotificationForError': emailNotificationForError,
            'emailNotificationEmail': emailNotificationEmail,
            'webNotificationUrl': webNotificationUrl,
            'webNotificationNotifyOncePerEmail': webNotificationNotifyOncePerEmail,
            'webNotificationForSent': webNotificationForSent,
            'webNotificationForOpened': webNotificationForOpened,
            'webNotificationForClicked': webNotificationForClicked,
            'webNotificationForUnsubscribed': webNotificationForUnsubscribed,
            'webNotificationForAbuseReport': webNotificationForAbuseReport,
            'webNotificationForError': webNotificationForError,
            'hubCallBackUrl': hubCallBackUrl,
            'inboundDomain': inboundDomain,
            'inboundContactsOnly': inboundContactsOnly,
            'lowCreditNotification': lowCreditNotification,
            'enableUITooltips': enableUITooltips,
            'enableContactFeatures': enableContactFeatures,
            'notificationsEmails': notificationsEmails,
            'unsubscribeNotificationsEmails': unsubscribeNotificationsEmails,
            'logoUrl': logoUrl,
            'enableTemplateScripting': enableTemplateScripting,
            'staleContactScore': staleContactScore,
            'staleContactInactiveDays': staleContactInactiveDays,
            'deliveryReason': deliveryReason,
            'tutorialsEnabled': tutorialsEnabled})

    def UpdateCustomBranding(enablePrivateBranding=False, logoUrl=None, supportLink=None, privateBrandingUrl=None, smtpAddress=None, smtpAlternative=None, paymentUrl=None):
        """
        Update settings of your private branding. These settings are needed, if you want to use Elastic Email under your brand.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool enablePrivateBranding - True: Turn on or off ability to send mails under your brand. Otherwise, false (default False)
            string logoUrl - URL to your logo image. (default None)
            string supportLink - Address to your support. (default None)
            string privateBrandingUrl - Subdomain for your rebranded service (default None)
            string smtpAddress - Address of SMTP server. (default None)
            string smtpAlternative - Address of alternative SMTP server. (default None)
            string paymentUrl - URL for making payments. (default None)
        """
        return ApiClient.Request('GET', '/account/updatecustombranding', {
            'enablePrivateBranding': enablePrivateBranding,
            'logoUrl': logoUrl,
            'supportLink': supportLink,
            'privateBrandingUrl': privateBrandingUrl,
            'smtpAddress': smtpAddress,
            'smtpAlternative': smtpAlternative,
            'paymentUrl': paymentUrl})

    def UpdateHttpNotification(url, notifyOncePerEmail=False, settings=None):
        """
        Update http notification URL.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string url - URL of notification.
            bool notifyOncePerEmail - True, if you want to receive notifications for each type only once per email. Otherwise, false (default False)
            string settings - Http notification settings serialized to JSON  (default None)
        """
        return ApiClient.Request('GET', '/account/updatehttpnotification', {
            'url': url,
            'notifyOncePerEmail': notifyOncePerEmail,
            'settings': settings})

    def UpdateProfile(firstName, lastName, address1, city, state, zip, countryID, marketingConsent=None, address2=None, company=None, website=None, logoUrl=None, taxCode=None, phone=None):
        """
        Update your profile.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string firstName - First name.
            string lastName - Last name.
            string address1 - First line of address.
            string city - City.
            string state - State or province.
            string zip - Zip/postal code.
            int countryID - Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
            bool? marketingConsent - True if you want to receive newsletters from Elastic Email. Otherwise, false. Empty to leave the current value. (default None)
            string address2 - Second line of address. (default None)
            string company - Company name. (default None)
            string website - HTTP address of your website. (default None)
            string logoUrl - URL to your logo image. (default None)
            string taxCode - Code used for tax purposes. (default None)
            string phone - Phone number (default None)
        """
        return ApiClient.Request('GET', '/account/updateprofile', {
            'firstName': firstName,
            'lastName': lastName,
            'address1': address1,
            'city': city,
            'state': state,
            'zip': zip,
            'countryID': countryID,
            'marketingConsent': marketingConsent,
            'address2': address2,
            'company': company,
            'website': website,
            'logoUrl': logoUrl,
            'taxCode': taxCode,
            'phone': phone})

    def UpdateSubAccountSettings(requiresEmailCredits=False, monthlyRefillCredits=0, requiresLitmusCredits=False, enableLitmusTest=False, dailySendLimit=None, emailSizeLimit=10, enablePrivateIPRequest=False, maxContacts=0, subAccountEmail=None, publicAccountID=None, sendingPermission=None, enableContactFeatures=None, poolName=None):
        """
        Updates settings of specified subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool requiresEmailCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            int monthlyRefillCredits - Amount of credits added to account automatically (default 0)
            bool requiresLitmusCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            bool enableLitmusTest - True, if account is able to send template tests to Litmus. Otherwise, false (default False)
            int? dailySendLimit - Amount of emails account can send daily (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            bool enablePrivateIPRequest - True, if account can request for private IP on its own. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the account can have (default 0)
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to update. Use subAccountEmail or publicAccountID not both. (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for account (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
        """
        return ApiClient.Request('GET', '/account/updatesubaccountsettings', {
            'requiresEmailCredits': requiresEmailCredits,
            'monthlyRefillCredits': monthlyRefillCredits,
            'requiresLitmusCredits': requiresLitmusCredits,
            'enableLitmusTest': enableLitmusTest,
            'dailySendLimit': dailySendLimit,
            'emailSizeLimit': emailSizeLimit,
            'enablePrivateIPRequest': enablePrivateIPRequest,
            'maxContacts': maxContacts,
            'subAccountEmail': subAccountEmail,
            'publicAccountID': publicAccountID,
            'sendingPermission': sendingPermission,
            'enableContactFeatures': enableContactFeatures,
            'poolName': poolName})


""" 
Sending and monitoring progress of your Campaigns
"""


class Campaign:

    def Add(campaign):
        """
        Adds a campaign to the queue for processing based on the configuration
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - Json representation of a campaign
        Returns int
        """
        return ApiClient.Request('GET', '/campaign/add', {
            'campaign': campaign})

    def Copy(channelID):
        """
        Copy selected campaign
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
        Returns int
        """
        return ApiClient.Request('GET', '/campaign/copy', {
            'channelID': channelID})

    def Delete(channelID):
        """
        Delete selected campaign
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
        """
        return ApiClient.Request('GET', '/campaign/delete', {
            'channelID': channelID})

    def Export(channelIDs={}, fileFormat=ApiTypes.ExportFileFormats.Csv, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export selected campaigns to chosen file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<int> channelIDs - List of campaign IDs used for processing (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/campaign/export', {
            'channelIDs': ";".join(map(str, channelIDs)),
            'fileFormat': fileFormat.value,
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def List(search=None, offset=0, limit=0):
        """
        List all of your campaigns
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string search - Text fragment used for searching. (default None)
            int offset - How many items should be loaded ahead. (default 0)
            int limit - Maximum of loaded items. (default 0)
        Returns List<ApiTypes.CampaignChannel>
        """
        return ApiClient.Request('GET', '/campaign/list', {
            'search': search,
            'offset': offset,
            'limit': limit})

    def Update(campaign):
        """
        Updates a previously added campaign.  Only Active and Paused campaigns can be updated.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - Json representation of a campaign
        Returns int
        """
        return ApiClient.Request('GET', '/campaign/update', {
            'campaign': campaign})


""" 
SMTP and HTTP API channels for grouping email delivery.
"""


class Channel:

    def Add(name):
        """
        Manually add a channel to your account to group email
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - Descriptive name of the channel
        Returns string
        """
        return ApiClient.Request('GET', '/channel/add', {
            'name': name})

    def Delete(name):
        """
        Delete the channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the channel to delete.
        """
        return ApiClient.Request('GET', '/channel/delete', {
            'name': name})

    def ExportCsv(channelNames, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export channels in CSV file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        return ApiClient.Request('GET', '/channel/exportcsv', {
            'channelNames': ";".join(map(str, channelNames)),
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def ExportJson(channelNames, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export channels in JSON file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        return ApiClient.Request('GET', '/channel/exportjson', {
            'channelNames': ";".join(map(str, channelNames)),
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def ExportXml(channelNames, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export channels in XML file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        return ApiClient.Request('GET', '/channel/exportxml', {
            'channelNames': ";".join(map(str, channelNames)),
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def List():
        """
        List all of your channels
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Channel>
        """
        return ApiClient.Request('GET', '/channel/list')

    def Update(name, newName):
        """
        Rename an existing channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the channel to update.
            string newName - The new name for the channel.
        Returns string
        """
        return ApiClient.Request('GET', '/channel/update', {
            'name': name,
            'newName': newName})


""" 
Methods used to manage your Contacts.
"""


class Contact:

    def Add(publicAccountID, email, publicListID={}, listName=[], firstName=None, lastName=None, source=ApiTypes.ContactSource.ContactApi, returnUrl=None, sourceUrl=None, activationReturnUrl=None, activationTemplate=None, sendActivation=True, consentDate=None, consentIP=None, field={}, notifyEmail=None):
        """
        Add a new contact and optionally to one of your lists.  Note that your API KEY is not required for this call.
            string publicAccountID - Public key for limited access to your account such as contact/add so you can use it safely on public websites.
            string email - Proper email address.
            IEnumerable<string> publicListID - ID code of list (default None)
            string[] listName - Name of your list. (default None)
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            ApiTypes.ContactSource source - Specifies the way of uploading the contact (default ApiTypes.ContactSource.ContactApi)
            string returnUrl - URL to navigate to after account creation (default None)
            string sourceUrl - URL from which request was sent. (default None)
            string activationReturnUrl - The url to return the contact to after activation. (default None)
            string activationTemplate -  (default None)
            bool sendActivation - True, if you want to send activation email to this account. Otherwise, false (default True)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
        Returns string
        """
        return ApiClient.Request('GET', '/contact/add', {
            'publicAccountID': publicAccountID,
            'email': email,
            'publicListID': ";".join(map(str, publicListID)),
            'listName': ";".join(map(str, listName)),
            'firstName': firstName,
            'lastName': lastName,
            'source': source.value,
            'returnUrl': returnUrl,
            'sourceUrl': sourceUrl,
            'activationReturnUrl': activationReturnUrl,
            'activationTemplate': activationTemplate,
            'sendActivation': sendActivation,
            'consentDate': consentDate,
            'consentIP': consentIP,
            'field': field,
            'notifyEmail': notifyEmail})

    def AddBlocked(email, status):
        """
        Manually add or update a contacts status to Abuse or Unsubscribed status (blocked).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        return ApiClient.Request('GET', '/contact/addblocked', {
            'email': email,
            'status': status.value})

    def ChangeProperty(email, name, value):
        """
        Change any property on the contact record.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string name - Name of the contact property you want to change.
            string value - Value you would like to change the contact property to.
        """
        return ApiClient.Request('GET', '/contact/changeproperty', {
            'email': email,
            'name': name,
            'value': value})

    def ChangeStatus(status, rule=None, emails={}):
        """
        Changes status of selected Contacts. You may provide RULE for selection or specify list of Contact IDs.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        return ApiClient.Request('GET', '/contact/changestatus', {
            'status': status.value,
            'rule': rule,
            'emails': ";".join(map(str, emails))})

    def CountByStatus(rule=None, allContacts=False):
        """
        Returns number of Contacts, RULE specifies contact Status.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns ApiTypes.ContactStatusCounts
        """
        return ApiClient.Request('GET', '/contact/countbystatus', {
            'rule': rule,
            'allContacts': allContacts})

    def CountByUnsubscribeReason(EEfrom=None, to=None):
        """
        Returns count of unsubscribe reasons for unsubscribed and complaint contacts.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
        Returns ApiTypes.ContactUnsubscribeReasonCounts
        """
        return ApiClient.Request('GET', '/contact/countbyunsubscribereason', {
            'from': EEfrom,
            'to': to})

    def Delete(rule=None, emails={}):
        """
        Permanantly deletes the contacts provided.  You can provide either a qualified rule or a list of emails (comma separated string).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        return ApiClient.Request('GET', '/contact/delete', {
            'rule': rule,
            'emails': ";".join(map(str, emails))})

    def Export(fileFormat=ApiTypes.ExportFileFormats.Csv, rule=None, emails={}, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export selected Contacts to file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/contact/export', {
            'fileFormat': fileFormat.value,
            'rule': rule,
            'emails': ";".join(map(str, emails)),
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def ExportUnsubscribeReasonCount(EEfrom=None, to=None, fileFormat=ApiTypes.ExportFileFormats.Csv, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export contacts' unsubscribe reasons count to file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/contact/exportunsubscribereasoncount', {
            'from': EEfrom,
            'to': to,
            'fileFormat': fileFormat.value,
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def FindContact(email):
        """
        Finds all Lists and Segments this email belongs to.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
        Returns ApiTypes.ContactCollection
        """
        return ApiClient.Request('GET', '/contact/findcontact', {
            'email': email})

    def GetContactsByList(listName, limit=20, offset=0):
        """
        List of Contacts for provided List
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        return ApiClient.Request('GET', '/contact/getcontactsbylist', {
            'listName': listName,
            'limit': limit,
            'offset': offset})

    def GetContactsBySegment(segmentName, limit=20, offset=0):
        """
        List of Contacts for provided Segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        return ApiClient.Request('GET', '/contact/getcontactsbysegment', {
            'segmentName': segmentName,
            'limit': limit,
            'offset': offset})

    def List(rule=None, limit=20, offset=0):
        """
        List of all contacts. If you have not specified RULE, all Contacts will be listed.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        return ApiClient.Request('GET', '/contact/list', {
            'rule': rule,
            'limit': limit,
            'offset': offset})

    def LoadBlocked(statuses, search=None, limit=0, offset=0):
        """
        Load blocked contacts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.ContactStatus> statuses - List of blocked statuses: Abuse, Bounced or Unsubscribed
            string search - Text fragment used for searching. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.BlockedContact>
        """
        return ApiClient.Request('GET', '/contact/loadblocked', {
            'statuses': ";".join(map(str, statuses)),
            'search': search,
            'limit': limit,
            'offset': offset})

    def LoadContact(email):
        """
        Load detailed contact information
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
        Returns ApiTypes.Contact
        """
        return ApiClient.Request('GET', '/contact/loadcontact', {
            'email': email})

    def LoadHistory(email, limit=0, offset=0):
        """
        Shows detailed history of chosen Contact.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.ContactHistory>
        """
        return ApiClient.Request('GET', '/contact/loadhistory', {
            'email': email,
            'limit': limit,
            'offset': offset})

    def QuickAdd(emails, firstName=None, lastName=None, publicListID=None, listName=None, status=ApiTypes.ContactStatus.Active, notes=None, consentDate=None, consentIP=None, field={}, notifyEmail=None):
        """
        Add new Contact to one of your Lists.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> emails - Comma delimited list of contact emails
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            string publicListID - ID code of list (default None)
            string listName - Name of your list. (default None)
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed. (default ApiTypes.ContactStatus.Active)
            string notes - Free form field of notes (default None)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
        """
        return ApiClient.Request('GET', '/contact/quickadd', {
            'emails': ";".join(map(str, emails)),
            'firstName': firstName,
            'lastName': lastName,
            'publicListID': publicListID,
            'listName': listName,
            'status': status.value,
            'notes': notes,
            'consentDate': consentDate,
            'consentIP': consentIP,
            'field': field,
            'notifyEmail': notifyEmail})

    def Subscribe(publicAccountID):
        """
        Basic double opt-in email subscribe form for your account.  This can be used for contacts that need to re-subscribe as well.
            string publicAccountID - Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        Returns string
        """
        return ApiClient.Request('GET', '/contact/subscribe', {
            'publicAccountID': publicAccountID})

    def Update(email, firstName=None, lastName=None, clearRestOfFields=True, field={}, customFields=None):
        """
        Update selected contact. Omitted contact's fields will be reset by default (see the clearRestOfFields parameter)
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            bool clearRestOfFields - States if the fields that were omitted in this request are to be reset or should they be left with their current value (default True)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string customFields - Custom contact field like firstname, lastname, city etc. JSON serialized text like { "city":"london" }  (default None)
        Returns ApiTypes.Contact
        """
        return ApiClient.Request('GET', '/contact/update', {
            'email': email,
            'firstName': firstName,
            'lastName': lastName,
            'clearRestOfFields': clearRestOfFields,
            'field': field,
            'customFields': customFields})

    def Upload(contactFile, allowUnsubscribe=False, listID=None, listName=None, status=ApiTypes.ContactStatus.Active, consentDate=None, consentIP=None):
        """
        Upload contacts in CSV file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File contactFile - Name of CSV file with Contacts.
            bool allowUnsubscribe - True: Allow unsubscribing from this (optional) newly created list. Otherwise, false (default False)
            int? listID - ID number of selected list. (default None)
            string listName - Name of your list to upload contacts to, or how the new, automatically created list should be named (default None)
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed. (default ApiTypes.ContactStatus.Active)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
        Returns int
        """
        attachments = []
        for name in contactFile:
            attachments.append(('attachments', open(name, 'rb')))
        return ApiClient.Request('POST', '/contact/upload', {
            'allowUnsubscribe': allowUnsubscribe,
            'listID': listID,
            'listName': listName,
            'status': status.value,
            'consentDate': consentDate,
            'consentIP': consentIP}, attachments)


""" 
Managing sender domains. Creating new entries and validating domain records.
"""


class Domain:

    def Add(domain, trackingType=ApiTypes.TrackingType.Http):
        """
        Add new domain to account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
        """
        return ApiClient.Request('GET', '/domain/add', {
            'domain': domain,
            'trackingType': trackingType.value})

    def Delete(domain):
        """
        Deletes configured domain from account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        """
        return ApiClient.Request('GET', '/domain/delete', {
            'domain': domain})

    def List():
        """
        Lists all domains configured for this account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.DomainDetail>
        """
        return ApiClient.Request('GET', '/domain/list')

    def SetDefault(domain):
        """
        Verification of email addres set for domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Default email sender, example: mail@yourdomain.com
        """
        return ApiClient.Request('GET', '/domain/setdefault', {
            'domain': domain})

    def VerifyDkim(domain):
        """
        Verification of DKIM record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        return ApiClient.Request('GET', '/domain/verifydkim', {
            'domain': domain})

    def VerifyMX(domain):
        """
        Verification of MX record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        return ApiClient.Request('GET', '/domain/verifymx', {
            'domain': domain})

    def VerifySpf(domain):
        """
        Verification of SPF record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        return ApiClient.Request('GET', '/domain/verifyspf', {
            'domain': domain})

    def VerifyTracking(domain, trackingType=ApiTypes.TrackingType.Http):
        """
        Verification of tracking CNAME record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
        Returns string
        """
        return ApiClient.Request('GET', '/domain/verifytracking', {
            'domain': domain,
            'trackingType': trackingType.value})


""" 

"""


class Email:

    def GetStatus(transactionID, showFailed=False, showSent=False, showDelivered=False, showPending=False, showOpened=False, showClicked=False, showAbuse=False, showUnsubscribed=False, showErrors=False, showMessageIDs=False):
        """
        Get email batch status
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string transactionID - Transaction identifier
            bool showFailed - Include Bounced email addresses. (default False)
            bool showSent - Include Sent email addresses. (default False)
            bool showDelivered - Include all delivered email addresses. (default False)
            bool showPending - Include Ready to send email addresses. (default False)
            bool showOpened - Include Opened email addresses. (default False)
            bool showClicked - Include Clicked email addresses. (default False)
            bool showAbuse - Include Reported as abuse email addresses. (default False)
            bool showUnsubscribed - Include Unsubscribed email addresses. (default False)
            bool showErrors - Include error messages for bounced emails. (default False)
            bool showMessageIDs - Include all MessageIDs for this transaction (default False)
        Returns ApiTypes.EmailJobStatus
        """
        return ApiClient.Request('GET', '/email/getstatus', {
            'transactionID': transactionID,
            'showFailed': showFailed,
            'showSent': showSent,
            'showDelivered': showDelivered,
            'showPending': showPending,
            'showOpened': showOpened,
            'showClicked': showClicked,
            'showAbuse': showAbuse,
            'showUnsubscribed': showUnsubscribed,
            'showErrors': showErrors,
            'showMessageIDs': showMessageIDs})

    def Send(subject=None, EEfrom=None, fromName=None, sender=None, senderName=None, msgFrom=None, msgFromName=None, replyTo=None, replyToName=None, to={}, msgTo={}, msgCC={}, msgBcc={}, lists={}, segments={}, mergeSourceFilename=None, dataSource=None, channel=None, bodyHtml=None, bodyText=None, charset=None, charsetBodyHtml=None, charsetBodyText=None, encodingType=ApiTypes.EncodingType.EENone, template=None, attachmentFiles={}, headers={}, postBack=None, merge={}, timeOffSetMinutes=None, poolName=None, isTransactional=False, attachments={}):
        """
        Submit emails. The HTTP POST request is suggested. The default, maximum (accepted by us) size of an email is 10 MB in total, with or without attachments included. For suggested implementations please refer to https://elasticemail.com/support/http-api/
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subject - Email subject (default None)
            string from - From email address (default None)
            string fromName - Display name for from email address (default None)
            string sender - Email address of the sender (default None)
            string senderName - Display name sender (default None)
            string msgFrom - Optional parameter. Sets FROM MIME header. (default None)
            string msgFromName - Optional parameter. Sets FROM name of MIME header. (default None)
            string replyTo - Email address to reply to (default None)
            string replyToName - Display name of the reply to address (default None)
            IEnumerable<string> to - List of email recipients (each email is treated separately, like a BCC). Separated by comma or semicolon. We suggest using the "msgTo" parameter if backward compatibility with API version 1 is not a must. (default None)
            IEnumerable<string> msgTo - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (visible to all other recipients of the message as TO MIME header). Separated by comma or semicolon. (default None)
            IEnumerable<string> msgCC - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (visible to all other recipients of the message as CC MIME header). Separated by comma or semicolon. (default None)
            IEnumerable<string> msgBcc - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (each email is treated seperately). Separated by comma or semicolon. (default None)
            IEnumerable<string> lists - The name of a contact list you would like to send to. Separate multiple contact lists by commas or semicolons. (default None)
            IEnumerable<string> segments - The name of a segment you would like to send to. Separate multiple segments by comma or semicolon. Insert "0" for all Active contacts. (default None)
            string mergeSourceFilename - File name one of attachments which is a CSV list of Recipients. (default None)
            string dataSource -  (default None)
            string channel - An ID field (max 191 chars) that can be used for reporting [will default to HTTP API or SMTP API] (default None)
            string bodyHtml - Html email body (default None)
            string bodyText - Text email body (default None)
            string charset - Text value of charset encoding for example: iso-8859-1, windows-1251, utf-8, us-ascii, windows-1250 and more… (default None)
            string charsetBodyHtml - Sets charset for body html MIME part (overrides default value from charset parameter) (default None)
            string charsetBodyText - Sets charset for body text MIME part (overrides default value from charset parameter) (default None)
            ApiTypes.EncodingType encodingType - 0 for None, 1 for Raw7Bit, 2 for Raw8Bit, 3 for QuotedPrintable, 4 for Base64 (Default), 5 for Uue  note that you can also provide the text version such as "Raw7Bit" for value 1.  NOTE: Base64 or QuotedPrintable is recommended if you are validating your domain(s) with DKIM. (default ApiTypes.EncodingType.EENone)
            string template - The ID of an email template you have created in your account. (default None)
            IEnumerableFile attachmentFiles - Attachment files. These files should be provided with the POST multipart file upload, not directly in the request's URL. Can also include merge CSV file (default None)
            Dictionary<string, string> headers - Optional Custom Headers. Request parameters prefixed by headers_ like headers_customheader1, headers_customheader2. Note: a space is required after the colon before the custom header value. headers_xmailer=xmailer: header-value1 (default None)
            string postBack - Optional header returned in notifications. (default None)
            Dictionary<string, string> merge - Request parameters prefixed by merge_ like merge_firstname, merge_lastname. If sending to a template you can send merge_ fields to merge data with the template. Template fields are entered with {firstname}, {lastname} etc. (default None)
            string timeOffSetMinutes - Number of minutes in the future this email should be sent up to a maximum of 1 year (524160 minutes) (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
            bool isTransactional - True, if email is transactional (non-bulk, non-marketing, non-commercial). Otherwise, false (default False)
            IEnumerable<string> attachments - Names or IDs of attachments previously uploaded to your account that should be sent with this e-mail. (default None)
        Returns ApiTypes.EmailSend
        """
        attachments = []
        for name in attachmentFiles:
            attachments.append(('attachments', open(name, 'rb')))
        return ApiClient.Request('POST', '/email/send', {
            'subject': subject,
            'from': EEfrom,
            'fromName': fromName,
            'sender': sender,
            'senderName': senderName,
            'msgFrom': msgFrom,
            'msgFromName': msgFromName,
            'replyTo': replyTo,
            'replyToName': replyToName,
            'to': ";".join(map(str, to)),
            'msgTo': ";".join(map(str, msgTo)),
            'msgCC': ";".join(map(str, msgCC)),
            'msgBcc': ";".join(map(str, msgBcc)),
            'lists': ";".join(map(str, lists)),
            'segments': ";".join(map(str, segments)),
            'mergeSourceFilename': mergeSourceFilename,
            'dataSource': dataSource,
            'channel': channel,
            'bodyHtml': bodyHtml,
            'bodyText': bodyText,
            'charset': charset,
            'charsetBodyHtml': charsetBodyHtml,
            'charsetBodyText': charsetBodyText,
            'encodingType': encodingType.value,
            'template': template,
            'headers': headers,
            'postBack': postBack,
            'merge': merge,
            'timeOffSetMinutes': timeOffSetMinutes,
            'poolName': poolName,
            'isTransactional': isTransactional,
            'attachments': ";".join(map(str, attachments))}, attachments)

    def Status(messageID):
        """
        Detailed status of a unique email sent through your account. Returns a 'Email has expired and the status is unknown.' error, if the email has not been fully processed yet.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string messageID - Unique identifier for this email.
        Returns ApiTypes.EmailStatus
        """
        return ApiClient.Request('GET', '/email/status', {
            'messageID': messageID})

    def View(messageID):
        """
        View email
            string messageID - Message identifier
        Returns ApiTypes.EmailView
        """
        return ApiClient.Request('GET', '/email/view', {
            'messageID': messageID})


""" 

"""


class Export:

    def CheckStatus(publicExportID):
        """
        Check the current status of the export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - 
        Returns ApiTypes.ExportStatus
        """
        return ApiClient.Request('GET', '/export/checkstatus', {
            'publicExportID': publicExportID})

    def CountByType():
        """
        Summary of export type counts.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.ExportTypeCounts
        """
        return ApiClient.Request('GET', '/export/countbytype')

    def Delete(publicExportID):
        """
        Delete the specified export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - 
        """
        return ApiClient.Request('GET', '/export/delete', {
            'publicExportID': publicExportID})

    def List(limit=0, offset=0):
        """
        Returns a list of all exported data.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Export>
        """
        return ApiClient.Request('GET', '/export/list', {
            'limit': limit,
            'offset': offset})


""" 
Manage the files on your account
"""


class File:

    def Delete(fileID=None, filename=None):
        """
        Permanently deletes the file from your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int? fileID -  (default None)
            string filename - Name of your file. (default None)
        """
        return ApiClient.Request('GET', '/file/delete', {
            'fileID': fileID,
            'filename': filename})

    def Download(filename=None, fileID=None):
        """
        Gets content of the chosen File
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file. (default None)
            int? fileID -  (default None)
        Returns File
        """
        return ApiClient.Request('GET', '/file/download', {
            'filename': filename,
            'fileID': fileID})

    def List(msgID):
        """
        Lists your available Attachments in the given email
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string msgID - ID number of selected message.
        Returns List<ApiTypes.File>
        """
        return ApiClient.Request('GET', '/file/list', {
            'msgID': msgID})

    def ListAll():
        """
        Lists all your available files
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.File>
        """
        return ApiClient.Request('GET', '/file/listall')

    def Load(filename):
        """
        Gets chosen File
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file.
        Returns ApiTypes.File
        """
        return ApiClient.Request('GET', '/file/load', {
            'filename': filename})

    def Upload(file, name=None, expiresAfterDays=30):
        """
        Uploads selected file to the server using http form upload format (MIME multipart/form-data) or PUT method.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File file - 
            string name - Filename (default None)
            int? expiresAfterDays - After how many days should the file be deleted. (default 30)
        Returns ApiTypes.File
        """
        attachments = []
        for name in file:
            attachments.append(('attachments', open(name, 'rb')))
        return ApiClient.Request('POST', '/file/upload', {
            'name': name,
            'expiresAfterDays': expiresAfterDays}, attachments)


""" 
API methods for managing your Lists
"""


class List:

    def Add(listName, createEmptyList=False, allowUnsubscribe=False, rule=None, emails={}, allContacts=False):
        """
        Create new list, based on filtering rule or list of IDs
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            bool createEmptyList - True to create an empty list, otherwise false. Ignores rule and emails parameters if provided. (default False)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns int
        """
        return ApiClient.Request('GET', '/list/add', {
            'listName': listName,
            'createEmptyList': createEmptyList,
            'allowUnsubscribe': allowUnsubscribe,
            'rule': rule,
            'emails': ";".join(map(str, emails)),
            'allContacts': allContacts})

    def AddContacts(listName, rule=None, emails={}, allContacts=False):
        """
        Add existing Contacts to chosen list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        """
        return ApiClient.Request('GET', '/list/addcontacts', {
            'listName': listName,
            'rule': rule,
            'emails': ";".join(map(str, emails)),
            'allContacts': allContacts})

    def Copy(sourceListName, newlistName=None, createEmptyList=None, allowUnsubscribe=None, rule=None):
        """
        Copy your existing List with the option to provide new settings to it. Some fields, when left empty, default to the source list's settings
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string sourceListName - The name of the list you want to copy
            string newlistName - Name of your list if you want to change it. (default None)
            bool? createEmptyList - True to create an empty list, otherwise false. Ignores rule and emails parameters if provided. (default None)
            bool? allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default None)
            string rule - Query used for filtering. (default None)
        Returns int
        """
        return ApiClient.Request('GET', '/list/copy', {
            'sourceListName': sourceListName,
            'newlistName': newlistName,
            'createEmptyList': createEmptyList,
            'allowUnsubscribe': allowUnsubscribe,
            'rule': rule})

    def CreateFromCampaign(campaignID, listName, statuses={}):
        """
        Create a new list from the recipients of the given campaign, using the given statuses of Messages
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int campaignID - ID of the campaign which recipients you want to copy
            string listName - Name of your list.
            IEnumerable<ApiTypes.LogJobStatus> statuses - Statuses of a campaign's emails you want to include in the new list (but NOT the contacts' statuses) (default None)
        Returns int
        """
        return ApiClient.Request('GET', '/list/createfromcampaign', {
            'campaignID': campaignID,
            'listName': listName,
            'statuses': ";".join(map(str, statuses))})

    def CreateNthSelectionLists(listName, numberOfLists, excludeBlocked=True, allowUnsubscribe=False, rule=None, allContacts=False):
        """
        Create a series of nth selection lists from an existing list or segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int numberOfLists - The number of evenly distributed lists to create.
            bool excludeBlocked - True if you want to exclude contacts that are currently in a blocked status of either unsubscribe, complaint or bounce. Otherwise, false. (default True)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        """
        return ApiClient.Request('GET', '/list/createnthselectionlists', {
            'listName': listName,
            'numberOfLists': numberOfLists,
            'excludeBlocked': excludeBlocked,
            'allowUnsubscribe': allowUnsubscribe,
            'rule': rule,
            'allContacts': allContacts})

    def CreateRandomList(listName, count, excludeBlocked=True, allowUnsubscribe=False, rule=None, allContacts=False):
        """
        Create a new list with randomized contacts from an existing list or segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int count - Number of items.
            bool excludeBlocked - True if you want to exclude contacts that are currently in a blocked status of either unsubscribe, complaint or bounce. Otherwise, false. (default True)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns int
        """
        return ApiClient.Request('GET', '/list/createrandomlist', {
            'listName': listName,
            'count': count,
            'excludeBlocked': excludeBlocked,
            'allowUnsubscribe': allowUnsubscribe,
            'rule': rule,
            'allContacts': allContacts})

    def Delete(listName):
        """
        Deletes List and removes all the Contacts from it (does not delete Contacts).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
        """
        return ApiClient.Request('GET', '/list/delete', {
            'listName': listName})

    def Export(listName, fileFormat=ApiTypes.ExportFileFormats.Csv, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Exports all the contacts from the provided list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/list/export', {
            'listName': listName,
            'fileFormat': fileFormat.value,
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def list(EEfrom=None, to=None):
        """
        Shows all your existing lists
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.List>
        """
        return ApiClient.Request('GET', '/list/list', {
            'from': EEfrom,
            'to': to})

    def Load(listName):
        """
        Returns detailed information about specific list.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
        Returns ApiTypes.List
        """
        return ApiClient.Request('GET', '/list/load', {
            'listName': listName})

    def MoveContacts(oldListName, newListName, emails={}, moveAll=None, statuses={}, rule=None):
        """
        Move selected contacts from one List to another
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string oldListName - The name of the list from which the contacts will be copied from
            string newListName - The name of the list to copy the contacts to
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool? moveAll - TRUE - moves all contacts; FALSE - moves contacts provided in the 'emails' parameter. This is ignored if the 'statuses' parameter has been provided (default None)
            IEnumerable<ApiTypes.ContactStatus> statuses - List of contact statuses which are eligible to move. This ignores the 'moveAll' parameter (default None)
            string rule - Query used for filtering. (default None)
        """
        return ApiClient.Request('GET', '/list/movecontacts', {
            'oldListName': oldListName,
            'newListName': newListName,
            'emails': ";".join(map(str, emails)),
            'moveAll': moveAll,
            'statuses': ";".join(map(str, statuses)),
            'rule': rule})

    def RemoveContacts(listName, rule=None, emails={}):
        """
        Remove selected Contacts from your list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        return ApiClient.Request('GET', '/list/removecontacts', {
            'listName': listName,
            'rule': rule,
            'emails': ";".join(map(str, emails))})

    def Update(listName, newListName=None, allowUnsubscribe=False):
        """
        Update existing list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string newListName - Name of your list if you want to change it. (default None)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
        """
        return ApiClient.Request('GET', '/list/update', {
            'listName': listName,
            'newListName': newListName,
            'allowUnsubscribe': allowUnsubscribe})


""" 
Methods to check logs of your campaigns
"""


class Log:

    def CancelInProgress(channelName=None, transactionID=None):
        """
        Cancels emails that are waiting to be sent.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string channelName - Name of selected channel. (default None)
            string transactionID - ID number of transaction (default None)
        """
        return ApiClient.Request('GET', '/log/cancelinprogress', {
            'channelName': channelName,
            'transactionID': transactionID})

    def Export(statuses, fileFormat=ApiTypes.ExportFileFormats.Csv, EEfrom=None, to=None, channelName=None, limit=0, offset=0, includeEmail=True, includeSms=True, messageCategory={}, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None, email=None):
        """
        Export email log information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            DateTime? from - Start date. (default None)
            DateTime? to - End date. (default None)
            string channelName - Name of selected channel. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            bool includeEmail - True: Search includes emails. Otherwise, false. (default True)
            bool includeSms - True: Search includes SMS. Otherwise, false. (default True)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
            string email - Proper email address. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/log/export', {
            'statuses': ";".join(map(str, statuses)),
            'fileFormat': fileFormat.value,
            'from': EEfrom,
            'to': to,
            'channelName': channelName,
            'limit': limit,
            'offset': offset,
            'includeEmail': includeEmail,
            'includeSms': includeSms,
            'messageCategory': ";".join(map(str, messageCategory)),
            'compressionFormat': compressionFormat.value,
            'fileName': fileName,
            'email': email})

    def ExportLinkTracking(EEfrom, to, channelName=None, fileFormat=ApiTypes.ExportFileFormats.Csv, limit=0, offset=0, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Export detailed link tracking information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            string channelName - Name of selected channel. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/log/exportlinktracking', {
            'from': EEfrom,
            'to': to,
            'channelName': channelName,
            'fileFormat': fileFormat.value,
            'limit': limit,
            'offset': offset,
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def LinkTracking(EEfrom=None, to=None, limit=0, offset=0, channelName=None):
        """
        Track link clicks
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            string channelName - Name of selected channel. (default None)
        Returns ApiTypes.LinkTrackingDetails
        """
        return ApiClient.Request('GET', '/log/linktracking', {
            'from': EEfrom,
            'to': to,
            'limit': limit,
            'offset': offset,
            'channelName': channelName})

    def Load(statuses, EEfrom=None, to=None, channelName=None, limit=0, offset=0, includeEmail=True, includeSms=True, messageCategory={}, email=None, useStatusChangeDate=False):
        """
        Returns logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            string channelName - Name of selected channel. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            bool includeEmail - True: Search includes emails. Otherwise, false. (default True)
            bool includeSms - True: Search includes SMS. Otherwise, false. (default True)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            string email - Proper email address. (default None)
            bool useStatusChangeDate - True, if 'from' and 'to' parameters should resolve to the Status Change date. To resolve to the creation date - false (default False)
        Returns ApiTypes.Log
        """
        return ApiClient.Request('GET', '/log/load', {
            'statuses': ";".join(map(str, statuses)),
            'from': EEfrom,
            'to': to,
            'channelName': channelName,
            'limit': limit,
            'offset': offset,
            'includeEmail': includeEmail,
            'includeSms': includeSms,
            'messageCategory': ";".join(map(str, messageCategory)),
            'email': email,
            'useStatusChangeDate': useStatusChangeDate})

    def LoadNotifications(statuses, EEfrom=None, to=None, limit=0, offset=0, messageCategory={}, useStatusChangeDate=False, notificationType=ApiTypes.NotificationType.All):
        """
        Returns notification logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            bool useStatusChangeDate - True, if 'from' and 'to' parameters should resolve to the Status Change date. To resolve to the creation date - false (default False)
            ApiTypes.NotificationType notificationType -  (default ApiTypes.NotificationType.All)
        Returns ApiTypes.Log
        """
        return ApiClient.Request('GET', '/log/loadnotifications', {
            'statuses': ";".join(map(str, statuses)),
            'from': EEfrom,
            'to': to,
            'limit': limit,
            'offset': offset,
            'messageCategory': ";".join(map(str, messageCategory)),
            'useStatusChangeDate': useStatusChangeDate,
            'notificationType': notificationType.value})

    def RetryNow(msgID):
        """
        Retry sending of temporarily not delivered message.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string msgID - ID number of selected message.
        """
        return ApiClient.Request('GET', '/log/retrynow', {
            'msgID': msgID})

    def Summary(EEfrom, to, channelName=None, interval=ApiTypes.IntervalType.Summary, transactionID=None):
        """
        Loads summary information about activity in chosen date range.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            string channelName - Name of selected channel. (default None)
            ApiTypes.IntervalType interval - 'Hourly' for detailed information, 'summary' for daily overview (default ApiTypes.IntervalType.Summary)
            string transactionID - ID number of transaction (default None)
        Returns ApiTypes.LogSummary
        """
        return ApiClient.Request('GET', '/log/summary', {
            'from': EEfrom,
            'to': to,
            'channelName': channelName,
            'interval': interval.value,
            'transactionID': transactionID})


""" 
Manages your segments - dynamically created lists of contacts
"""


class Segment:

    def Add(segmentName, rule):
        """
        Create new segment, based on specified RULE.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            string rule - Query used for filtering.
        Returns ApiTypes.Segment
        """
        return ApiClient.Request('GET', '/segment/add', {
            'segmentName': segmentName,
            'rule': rule})

    def Copy(sourceSegmentName, newSegmentName=None, rule=None):
        """
        Copy your existing Segment with the optional new rule and custom name
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string sourceSegmentName - The name of the segment you want to copy
            string newSegmentName - New name of your segment if you want to change it. (default None)
            string rule - Query used for filtering. (default None)
        Returns ApiTypes.Segment
        """
        return ApiClient.Request('GET', '/segment/copy', {
            'sourceSegmentName': sourceSegmentName,
            'newSegmentName': newSegmentName,
            'rule': rule})

    def Delete(segmentName):
        """
        Delete existing segment.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
        """
        return ApiClient.Request('GET', '/segment/delete', {
            'segmentName': segmentName})

    def Export(segmentName, fileFormat=ApiTypes.ExportFileFormats.Csv, compressionFormat=ApiTypes.CompressionFormat.EENone, fileName=None):
        """
        Exports all the contacts from the provided segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/segment/export', {
            'segmentName': segmentName,
            'fileFormat': fileFormat.value,
            'compressionFormat': compressionFormat.value,
            'fileName': fileName})

    def List(includeHistory=False, EEfrom=None, to=None):
        """
        Lists all your available Segments
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool includeHistory - True: Include history of last 30 days. Otherwise, false. (default False)
            DateTime? from - From what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - To what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.Segment>
        """
        return ApiClient.Request('GET', '/segment/list', {
            'includeHistory': includeHistory,
            'from': EEfrom,
            'to': to})

    def LoadByName(segmentNames, includeHistory=False, EEfrom=None, to=None):
        """
        Lists your available Segments using the provided names
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> segmentNames - Names of segments you want to load. Will load all contacts if left empty or the 'All Contacts' name has been provided
            bool includeHistory - True: Include history of last 30 days. Otherwise, false. (default False)
            DateTime? from - From what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - To what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.Segment>
        """
        return ApiClient.Request('GET', '/segment/loadbyname', {
            'segmentNames': ";".join(map(str, segmentNames)),
            'includeHistory': includeHistory,
            'from': EEfrom,
            'to': to})

    def Update(segmentName, newSegmentName=None, rule=None):
        """
        Rename or change RULE for your segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            string newSegmentName - New name of your segment if you want to change it. (default None)
            string rule - Query used for filtering. (default None)
        Returns ApiTypes.Segment
        """
        return ApiClient.Request('GET', '/segment/update', {
            'segmentName': segmentName,
            'newSegmentName': newSegmentName,
            'rule': rule})


""" 
Managing texting to your clients.
"""


class SMS:

    def Send(to, body):
        """
        Send a short SMS Message (maximum of 1600 characters) to any mobile phone.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string to - Mobile number you want to message. Can be any valid mobile number in E.164 format. To provide the country code you need to provide "+" before the number.  If your URL is not encoded then you need to replace the "+" with "%2B" instead.
            string body - Body of your message. The maximum body length is 160 characters.  If the message body is greater than 160 characters it is split into multiple messages and you are charged per message for the number of message required to send your length
        """
        return ApiClient.Request('GET', '/sms/send', {
            'to': to,
            'body': body})


""" 
Methods to organize and get results of your surveys
"""


class Survey:

    def Add(survey):
        """
        Adds a new survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Survey survey - Json representation of a survey
        Returns ApiTypes.Survey
        """
        return ApiClient.Request('GET', '/survey/add', {
            'survey': survey})

    def Delete(publicSurveyID):
        """
        Deletes the survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        """
        return ApiClient.Request('GET', '/survey/delete', {
            'publicSurveyID': publicSurveyID})

    def Export(publicSurveyID, fileName, fileFormat=ApiTypes.ExportFileFormats.Csv, compressionFormat=ApiTypes.CompressionFormat.EENone):
        """
        Export given survey's data to provided format
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
            string fileName - Name of your file.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
        Returns ApiTypes.ExportLink
        """
        return ApiClient.Request('GET', '/survey/export', {
            'publicSurveyID': publicSurveyID,
            'fileName': fileName,
            'fileFormat': fileFormat.value,
            'compressionFormat': compressionFormat.value})

    def List():
        """
        Shows all your existing surveys
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Survey>
        """
        return ApiClient.Request('GET', '/survey/list')

    def LoadResponseList(publicSurveyID):
        """
        Get list of personal answers for the specific survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        Returns List<ApiTypes.SurveyResultInfo>
        """
        return ApiClient.Request('GET', '/survey/loadresponselist', {
            'publicSurveyID': publicSurveyID})

    def LoadResults(publicSurveyID):
        """
        Get general results of the specific survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        Returns ApiTypes.SurveyResultsSummaryInfo
        """
        return ApiClient.Request('GET', '/survey/loadresults', {
            'publicSurveyID': publicSurveyID})

    def Update(survey):
        """
        Update the survey information
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Survey survey - Json representation of a survey
        Returns ApiTypes.Survey
        """
        return ApiClient.Request('GET', '/survey/update', {
            'survey': survey})


""" 
Managing and editing templates of your emails
"""


class Template:

    def Add(templateName, subject, fromEmail, fromName, templateType=ApiTypes.TemplateType.RawHTML, templateScope=ApiTypes.TemplateScope.Private, bodyHtml=None, bodyText=None, css=None, originalTemplateID=0):
        """
        Create new Template. Needs to be sent using POST method
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string templateName - Name of template.
            string subject - Default subject of email.
            string fromEmail - Default From: email address.
            string fromName - Default From: name.
            ApiTypes.TemplateType templateType - 0 for API connections (default ApiTypes.TemplateType.RawHTML)
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
            string bodyHtml - HTML code of email (needs escaping). (default None)
            string bodyText - Text body of email. (default None)
            string css - CSS style (default None)
            int originalTemplateID - ID number of original template. (default 0)
        Returns int
        """
        return ApiClient.Request('GET', '/template/add', {
            'templateName': templateName,
            'subject': subject,
            'fromEmail': fromEmail,
            'fromName': fromName,
            'templateType': templateType.value,
            'templateScope': templateScope.value,
            'bodyHtml': bodyHtml,
            'bodyText': bodyText,
            'css': css,
            'originalTemplateID': originalTemplateID})

    def CheckUsage(templateID):
        """
        Check if template is used by campaign.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns bool
        """
        return ApiClient.Request('GET', '/template/checkusage', {
            'templateID': templateID})

    def Copy(templateID, templateName, subject, fromEmail, fromName):
        """
        Copy Selected Template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            string templateName - Name of template.
            string subject - Default subject of email.
            string fromEmail - Default From: email address.
            string fromName - Default From: name.
        Returns ApiTypes.Template
        """
        return ApiClient.Request('GET', '/template/copy', {
            'templateID': templateID,
            'templateName': templateName,
            'subject': subject,
            'fromEmail': fromEmail,
            'fromName': fromName})

    def Delete(templateID):
        """
        Delete template with the specified ID
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        """
        return ApiClient.Request('GET', '/template/delete', {
            'templateID': templateID})

    def GetEmbeddedHtml(templateID):
        """
        Search for references to images and replaces them with base64 code.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns string
        """
        return ApiClient.Request('GET', '/template/getembeddedhtml', {
            'templateID': templateID})

    def GetList(limit=500, offset=0):
        """
        Lists your templates
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 500)
            int offset - How many items should be loaded ahead. (default 0)
        Returns ApiTypes.TemplateList
        """
        return ApiClient.Request('GET', '/template/getlist', {
            'limit': limit,
            'offset': offset})

    def LoadTemplate(templateID, ispublic=False):
        """
        Load template with content
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            bool ispublic -  (default False)
        Returns ApiTypes.Template
        """
        return ApiClient.Request('GET', '/template/loadtemplate', {
            'templateID': templateID,
            'ispublic': ispublic})

    def RemoveScreenshot(templateID):
        """
        Removes previously generated screenshot of template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        """
        return ApiClient.Request('GET', '/template/removescreenshot', {
            'templateID': templateID})

    def SaveScreenshot(base64Image, templateID):
        """
        Saves screenshot of chosen Template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string base64Image - Image, base64 coded.
            int templateID - ID number of template.
        Returns string
        """
        return ApiClient.Request('GET', '/template/savescreenshot', {
            'base64Image': base64Image,
            'templateID': templateID})

    def Update(templateID, templateScope=ApiTypes.TemplateScope.Private, templateName=None, subject=None, fromEmail=None, fromName=None, bodyHtml=None, bodyText=None, css=None, removeScreenshot=True):
        """
        Update existing template, overwriting existing data. Needs to be sent using POST method.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
            string templateName - Name of template. (default None)
            string subject - Default subject of email. (default None)
            string fromEmail - Default From: email address. (default None)
            string fromName - Default From: name. (default None)
            string bodyHtml - HTML code of email (needs escaping). (default None)
            string bodyText - Text body of email. (default None)
            string css - CSS style (default None)
            bool removeScreenshot -  (default True)
        """
        return ApiClient.Request('GET', '/template/update', {
            'templateID': templateID,
            'templateScope': templateScope.value,
            'templateName': templateName,
            'subject': subject,
            'fromEmail': fromEmail,
            'fromName': fromName,
            'bodyHtml': bodyHtml,
            'bodyText': bodyText,
            'css': css,
            'removeScreenshot': removeScreenshot})
