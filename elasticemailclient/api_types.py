from enum import Enum


class ApiTypes:
    """
    Detailed information about your account
    """
    class Account:
        """
        Code used for tax purposes.
        """
        TaxCode = None  # string

        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None  # string

        """
        ApiKey that gives you access to our SMTP and HTTP API's.
        """
        ApiKey = None  # string

        """
        Second ApiKey that gives you access to our SMTP and HTTP API's.  Used mainly for changing ApiKeys without disrupting services.
        """
        ApiKey2 = None  # string

        """
        True, if account is a subaccount. Otherwise, false
        """
        IsSub = None  # bool

        """
        The number of subaccounts this account has.
        """
        SubAccountsCount = None  # long

        """
        Number of status: 1 - Active
        """
        StatusNumber = None  # int

        """
        Account status: Active
        """
        StatusFormatted = None  # string

        """
        URL form for payments.
        """
        PaymentFormUrl = None  # string

        """
        URL to your logo image.
        """
        LogoUrl = None  # string

        """
        HTTP address of your website.
        """
        Website = None  # string

        """
        True: Turn on or off ability to send mails under your brand. Otherwise, false
        """
        EnablePrivateBranding = None  # bool

        """
        Address to your support.
        """
        SupportLink = None  # string

        """
        Subdomain for your rebranded service
        """
        PrivateBrandingUrl = None  # string

        """
        First name.
        """
        FirstName = None  # string

        """
        Last name.
        """
        LastName = None  # string

        """
        Company name.
        """
        Company = None  # string

        """
        First line of address.
        """
        Address1 = None  # string

        """
        Second line of address.
        """
        Address2 = None  # string

        """
        City.
        """
        City = None  # string

        """
        State or province.
        """
        State = None  # string

        """
        Zip/postal code.
        """
        Zip = None  # string

        """
        Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
        """
        CountryID = None  # int?

        """
        Phone number
        """
        Phone = None  # string

        """
        Proper email address.
        """
        Email = None  # string

        """
        URL for affiliating.
        """
        AffiliateLink = None  # string

        """
        Numeric reputation
        """
        Reputation = None  # double

        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None  # long

        """
        Amount of emails sent from this account
        """
        MonthlyEmailsSent = None  # long?

        """
        Amount of emails sent from this account
        """
        Credit = None  # decimal

        """
        Amount of email credits
        """
        EmailCredits = None  # int

        """
        Amount of emails sent from this account
        """
        PricePerEmail = None  # decimal

        """
        Why your clients are receiving your emails.
        """
        DeliveryReason = None  # string

        """
        URL for making payments.
        """
        AccountPaymentUrl = None  # string

        """
        Address of SMTP server.
        """
        Smtp = None  # string

        """
        Address of alternative SMTP server.
        """
        SmtpAlternative = None  # string

        """
        Status of automatic payments configuration.
        """
        AutoCreditStatus = None  # string

        """
        When AutoCreditStatus is Enabled, the credit level that triggers the credit to be recharged.
        """
        AutoCreditLevel = None  # decimal

        """
        When AutoCreditStatus is Enabled, the amount of credit to be recharged.
        """
        AutoCreditAmount = None  # decimal

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None  # int

        """
        Creation date.
        """
        DateCreated = None  # DateTime

        """
        True, if you have enabled link tracking. Otherwise, false
        """
        LinkTracking = None  # bool

        """
        Type of content encoding
        """
        ContentTransferEncoding = None  # string

        """
        Amount of Litmus credits
        """
        LitmusCredits = None  # decimal

        """
        Enable contact delivery and optimization tools on your Account.
        """
        EnableContactFeatures = None  # bool

        """
        
        """
        NeedsSMSVerification = None  # bool

        """
        
        """
        EnableBouncesHandling = None  # bool

    """
    Basic overview of your account
    """
    class AccountOverview:
        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None  # long

        """
        Amount of emails sent from this account
        """
        Credit = None  # decimal

        """
        Cost of 1000 emails
        """
        CostPerThousand = None  # decimal

        """
        Number of messages in progress
        """
        InProgressCount = None  # long

        """
        Number of contacts currently with blocked status of Unsubscribed, Complaint, Bounced or InActive
        """
        BlockedContactsCount = None  # long

        """
        Numeric reputation
        """
        Reputation = None  # double

        """
        Number of contacts
        """
        ContactCount = None  # long

        """
        Number of created campaigns
        """
        CampaignCount = None  # long

        """
        Number of available templates
        """
        TemplateCount = None  # long

        """
        Number of created subaccounts
        """
        SubAccountCount = None  # long

        """
        Number of active referrals
        """
        ReferralCount = None  # long

    """
    Lists advanced sending options of your account.
    """
    class AdvancedOptions:
        """
        True, if you want to track clicks. Otherwise, false
        """
        EnableClickTracking = None  # bool

        """
        True, if you want to track by link tracking. Otherwise, false
        """
        EnableLinkClickTracking = None  # bool

        """
        True, if you want to use template scripting in your emails {{}}. Otherwise, false
        """
        EnableTemplateScripting = None  # bool

        """
        True, if text BODY of message should be created automatically. Otherwise, false
        """
        AutoTextFormat = None  # bool

        """
        True, if you want bounce notifications returned. Otherwise, false
        """
        EmailNotificationForError = None  # bool

        """
        True, if you want to send web notifications for sent email. Otherwise, false
        """
        WebNotificationForSent = None  # bool

        """
        True, if you want to send web notifications for opened email. Otherwise, false
        """
        WebNotificationForOpened = None  # bool

        """
        True, if you want to send web notifications for clicked email. Otherwise, false
        """
        WebNotificationForClicked = None  # bool

        """
        True, if you want to send web notifications for unsubscribed email. Otherwise, false
        """
        WebnotificationForUnsubscribed = None  # bool

        """
        True, if you want to send web notifications for complaint email. Otherwise, false
        """
        WebNotificationForAbuse = None  # bool

        """
        True, if you want to send web notifications for bounced email. Otherwise, false
        """
        WebNotificationForError = None  # bool

        """
        True, if you want to receive notifications for each type only once per email. Otherwise, false
        """
        WebNotificationNotifyOncePerEmail = None  # bool

        """
        True, if you want to receive low credit email notifications. Otherwise, false
        """
        LowCreditNotification = None  # bool

        """
        True, if you want inbound email to only process contacts from your account. Otherwise, false
        """
        InboundContactsOnly = None  # bool

        """
        True, if this account is a sub-account. Otherwise, false
        """
        IsSubAccount = None  # bool

        """
        True, if this account resells Elastic Email. Otherwise, false.
        """
        IsOwnedByReseller = None  # bool

        """
        True, if you want to enable list-unsubscribe header. Otherwise, false
        """
        EnableUnsubscribeHeader = None  # bool

        """
        True, if you want to display your labels on your unsubscribe form. Otherwise, false
        """
        ManageSubscriptions = None  # bool

        """
        True, if you want to only display labels that the contact is subscribed to on your unsubscribe form. Otherwise, false
        """
        ManageSubscribedOnly = None  # bool

        """
        True, if you want to display an option for the contact to opt into transactional email only on your unsubscribe form. Otherwise, false
        """
        TransactionalOnUnsubscribe = None  # bool

        """
        
        """
        PreviewMessageID = None  # string

        """
        True, if you want to apply custom headers to your emails. Otherwise, false
        """
        AllowCustomHeaders = None  # bool

        """
        Email address to send a copy of all email to.
        """
        BccEmail = None  # string

        """
        Type of content encoding
        """
        ContentTransferEncoding = None  # string

        """
        True, if you want to receive bounce email notifications. Otherwise, false
        """
        EmailNotification = None  # string

        """
        Email addresses to send a copy of all notifications from our system. Separated by semicolon
        """
        NotificationsEmails = None  # string

        """
        Emails, separated by semicolon, to which the notification about contact unsubscribing should be sent to
        """
        UnsubscribeNotificationEmails = None  # string

        """
        URL address to receive web notifications to parse and process.
        """
        WebNotificationUrl = None  # string

        """
        URL used for tracking action of inbound emails
        """
        HubCallbackUrl = None  # string

        """
        Domain you use as your inbound domain
        """
        InboundDomain = None  # string

        """
        True, if account has tooltips active. Otherwise, false
        """
        EnableUITooltips = None  # bool

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None  # bool

        """
        URL to your logo image.
        """
        LogoUrl = None  # string

        """
        (0 means this functionality is NOT enabled) Score, depending on the number of times you have sent to a recipient, at which the given recipient should be moved to the Stale status
        """
        StaleContactScore = None  # int

        """
        (0 means this functionality is NOT enabled) Number of days of inactivity for a contact after which the given recipient should be moved to the Stale status
        """
        StaleContactInactiveDays = None  # int

        """
        Why your clients are receiving your emails.
        """
        DeliveryReason = None  # string

    """
    
    """
    class APIKeyAction(Enum):
        """
        Add an additional APIKey to your Account.
        """
        Add = 1

        """
        Change this APIKey to a new one.
        """
        Change = 2

        """
        Delete this APIKey
        """
        Delete = 3

    """
    Blocked Contact - Contact returning Hard Bounces
    """
    class BlockedContact:
        """
        Proper email address.
        """
        Email = None  # string

        """
        Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        Status = None  # string

        """
        RFC error message
        """
        FriendlyErrorMessage = None  # string

        """
        Last change date
        """
        DateUpdated = None  # string

    """
    Summary of bounced categories, based on specified date range.
    """
    class BouncedCategorySummary:
        """
        Number of messages marked as SPAM
        """
        Spam = None  # long

        """
        Number of blacklisted messages
        """
        BlackListed = None  # long

        """
        Number of messages flagged with 'No Mailbox'
        """
        NoMailbox = None  # long

        """
        Number of messages flagged with 'Grey Listed'
        """
        GreyListed = None  # long

        """
        Number of messages flagged with 'Throttled'
        """
        Throttled = None  # long

        """
        Number of messages flagged with 'Timeout'
        """
        Timeout = None  # long

        """
        Number of messages flagged with 'Connection Problem'
        """
        ConnectionProblem = None  # long

        """
        Number of messages flagged with 'SPF Problem'
        """
        SpfProblem = None  # long

        """
        Number of messages flagged with 'Account Problem'
        """
        AccountProblem = None  # long

        """
        Number of messages flagged with 'DNS Problem'
        """
        DnsProblem = None  # long

        """
        Number of messages flagged with 'WhiteListing Problem'
        """
        WhitelistingProblem = None  # long

        """
        Number of messages flagged with 'Code Error'
        """
        CodeError = None  # long

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None  # long

        """
        Number of manually cancelled messages
        """
        ManualCancel = None  # long

        """
        Number of messages flagged with 'Connection terminated'
        """
        ConnectionTerminated = None  # long

    """
    Campaign
    """
    class Campaign:
        """
        ID number of selected Channel.
        """
        ChannelID = None  # int?

        """
        Campaign's name
        """
        Name = None  # string

        """
        Name of campaign's status
        """
        Status = None  # ApiTypes.CampaignStatus

        """
        List of Segment and List IDs, preceded with 'l' for Lists and 's' for Segments, comma separated
        """
        Targets = None  # string[]

        """
        Number of event, triggering mail sending
        """
        TriggerType = None  # ApiTypes.CampaignTriggerType

        """
        Date of triggered send
        """
        TriggerDate = None  # DateTime?

        """
        How far into the future should the campaign be sent, in minutes
        """
        TriggerDelay = None  # double

        """
        When your next automatic mail will be sent, in minutes
        """
        TriggerFrequency = None  # double

        """
        How many times should the campaign be sent
        """
        TriggerCount = None  # int

        """
        ID number of transaction
        """
        TriggerChannelID = None  # int

        """
        Data for filtering event campaigns such as specific link addresses.
        """
        TriggerData = None  # string

        """
        What should be checked for choosing the winner: opens or clicks
        """
        SplitOptimization = None  # ApiTypes.SplitOptimization

        """
        Number of minutes between sends during optimization period
        """
        SplitOptimizationMinutes = None  # int

        """
        
        """
        TimingOption = None  # int

        """
        
        """
        CampaignTemplates = None  # List<ApiTypes.CampaignTemplate>

    """
    Channel
    """
    class CampaignChannel:
        """
        ID number of selected Channel.
        """
        ChannelID = None  # int

        """
        Filename
        """
        Name = None  # string

        """
        True, if you are sending a campaign. Otherwise, false.
        """
        IsCampaign = None  # bool

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None  # string

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None  # DateTime

        """
        Name of campaign's status
        """
        Status = None  # ApiTypes.CampaignStatus

        """
        Date of last activity on account
        """
        LastActivity = None  # DateTime?

        """
        Datetime of last action done on campaign.
        """
        LastProcessed = None  # DateTime?

        """
        Id number of parent channel
        """
        ParentChannelID = None  # int

        """
        List of Segment and List IDs, preceded with 'l' for Lists and 's' for Segments, comma separated
        """
        Targets = None  # string[]

        """
        Number of event, triggering mail sending
        """
        TriggerType = None  # ApiTypes.CampaignTriggerType

        """
        Date of triggered send
        """
        TriggerDate = None  # DateTime?

        """
        How far into the future should the campaign be sent, in minutes
        """
        TriggerDelay = None  # double

        """
        When your next automatic mail will be sent, in minutes
        """
        TriggerFrequency = None  # double

        """
        How many times should the campaign be sent
        """
        TriggerCount = None  # int

        """
        ID number of transaction
        """
        TriggerChannelID = None  # int

        """
        Data for filtering event campaigns such as specific link addresses.
        """
        TriggerData = None  # string

        """
        What should be checked for choosing the winner: opens or clicks
        """
        SplitOptimization = None  # ApiTypes.SplitOptimization

        """
        Number of minutes between sends during optimization period
        """
        SplitOptimizationMinutes = None  # int

        """
        
        """
        TimingOption = None  # int

        """
        ID number of template.
        """
        TemplateID = None  # int?

        """
        Default subject of email.
        """
        TemplateSubject = None  # string

        """
        Default From: email address.
        """
        TemplateFromEmail = None  # string

        """
        Default From: name.
        """
        TemplateFromName = None  # string

        """
        Default Reply: email address.
        """
        TemplateReplyEmail = None  # string

        """
        Default Reply: name.
        """
        TemplateReplyName = None  # string

        """
        Total emails clicked
        """
        ClickedCount = None  # int

        """
        Total emails opened.
        """
        OpenedCount = None  # int

        """
        Overall number of recipients
        """
        RecipientCount = None  # int

        """
        Total emails sent.
        """
        SentCount = None  # int

        """
        Total emails sent.
        """
        FailedCount = None  # int

        """
        Total emails clicked
        """
        UnsubscribedCount = None  # int

        """
        Abuses - mails sent to user without their consent
        """
        FailedAbuse = None  # int

        """
        List of CampaignTemplate for sending A-X split testing.
        """
        TemplateChannels = None  # List<ApiTypes.CampaignChannel>

    """
    
    """
    class CampaignStatus(Enum):
        """
        Campaign is logically deleted and not returned by API or interface calls.
        """
        Deleted = -1

        """
        Campaign is curently active and available.
        """
        Active = 0

        """
        Campaign is currently being processed for delivery.
        """
        Processing = 1

        """
        Campaign is currently sending.
        """
        Sending = 2

        """
        Campaign has completed sending.
        """
        Completed = 3

        """
        Campaign is currently paused and not sending.
        """
        Paused = 4

        """
        Campaign has been cancelled during delivery.
        """
        Cancelled = 5

        """
        Campaign is save as draft and not processing.
        """
        Draft = 6

    """
    
    """
    class CampaignTemplate:
        """
        ID number of selected Channel.
        """
        ChannelID = None  # int?

        """
        Name of campaign's status
        """
        Status = None  # ApiTypes.CampaignStatus

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None  # string

        """
        ID number of template.
        """
        TemplateID = None  # int?

        """
        Default subject of email.
        """
        TemplateSubject = None  # string

        """
        Default From: email address.
        """
        TemplateFromEmail = None  # string

        """
        Default From: name.
        """
        TemplateFromName = None  # string

        """
        Default Reply: email address.
        """
        TemplateReplyEmail = None  # string

        """
        Default Reply: name.
        """
        TemplateReplyName = None  # string

    """
    
    """
    class CampaignTriggerType(Enum):
        """

        """
        SendNow = 1

        """
        
        """
        FutureScheduled = 2

        """
        
        """
        OnAdd = 3

        """
        
        """
        OnOpen = 4

        """
        
        """
        OnClick = 5

    """
    
    """
    class CertificateValidationStatus(Enum):
        """

        """
        ErrorOccured = -2

        """
        
        """
        CertNotSet = 0

        """
        
        """
        Valid = 1

        """
        
        """
        NotValid = 2

    """
    SMTP and HTTP API channel for grouping email delivery
    """
    class Channel:
        """
        Descriptive name of the channel.
        """
        Name = None  # string

        """
        The date the channel was added to your account.
        """
        DateAdded = None  # DateTime

        """
        The date the channel was last sent through.
        """
        LastActivity = None  # DateTime?

        """
        The number of email jobs this channel has been used with.
        """
        JobCount = None  # int

        """
        The number of emails that have been clicked within this channel.
        """
        ClickedCount = None  # int

        """
        The number of emails that have been opened within this channel.
        """
        OpenedCount = None  # int

        """
        The number of emails attempted to be sent within this channel.
        """
        RecipientCount = None  # int

        """
        The number of emails that have been sent within this channel.
        """
        SentCount = None  # int

        """
        The number of emails that have been bounced within this channel.
        """
        FailedCount = None  # int

        """
        The number of emails that have been unsubscribed within this channel.
        """
        UnsubscribedCount = None  # int

        """
        The number of emails that have been marked as abuse or complaint within this channel.
        """
        FailedAbuse = None  # int

        """
        The total cost for emails/attachments within this channel.
        """
        Cost = None  # decimal

    """
    FileResponse compression format
    """
    class CompressionFormat(Enum):
        """
        No compression
        """
        EENone = 0

        """
        Zip compression
        """
        Zip = 1

    """
    Contact
    """
    class Contact:
        """

        """
        ContactScore = None  # int

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None  # DateTime

        """
        Proper email address.
        """
        Email = None  # string

        """
        First name.
        """
        FirstName = None  # string

        """
        Last name.
        """
        LastName = None  # string

        """
        Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        Status = None  # ApiTypes.ContactStatus

        """
        RFC Error code
        """
        BouncedErrorCode = None  # int?

        """
        RFC error message
        """
        BouncedErrorMessage = None  # string

        """
        Total emails sent.
        """
        TotalSent = None  # int

        """
        Total emails sent.
        """
        TotalFailed = None  # int

        """
        Total emails opened.
        """
        TotalOpened = None  # int

        """
        Total emails clicked
        """
        TotalClicked = None  # int

        """
        Date of first failed message
        """
        FirstFailedDate = None  # DateTime?

        """
        Number of fails in sending to this Contact
        """
        LastFailedCount = None  # int

        """
        Last change date
        """
        DateUpdated = None  # DateTime

        """
        Source of URL of payment
        """
        Source = None  # ApiTypes.ContactSource

        """
        RFC Error code
        """
        ErrorCode = None  # int?

        """
        RFC error message
        """
        FriendlyErrorMessage = None  # string

        """
        IP address
        """
        CreatedFromIP = None  # string

        """
        Unsubscribed date in YYYY-MM-DD format
        """
        UnsubscribedDate = None  # DateTime?

        """
        Free form field of notes
        """
        Notes = None  # string

        """
        Website of contact
        """
        WebsiteUrl = None  # string

        """
        Date this contact last opened an email
        """
        LastOpened = None  # DateTime?

        """
        
        """
        LastClicked = None  # DateTime?

        """
        Custom contact field like firstname, lastname, city etc. JSON serialized text like { "city":"london" } 
        """
        CustomFields = None  # Dictionary<string, string>

    """
    Collection of lists and segments
    """
    class ContactCollection:
        """
        Lists which contain the requested contact
        """
        Lists = None  # List<ApiTypes.ContactContainer>

        """
        Segments which contain the requested contact
        """
        Segments = None  # List<ApiTypes.ContactContainer>

    """
    List's or segment's short info
    """
    class ContactContainer:
        """
        ID of the list/segment
        """
        ID = None  # int

        """
        Name of the list/segment
        """
        Name = None  # string

    """
    
    """
    class ContactHistEventType(Enum):
        """
        Contact opened an e-mail
        """
        Opened = 2

        """
        Contact clicked an e-mail
        """
        Clicked = 3

        """
        E-mail sent to the contact bounced
        """
        Bounced = 10

        """
        Contact unsubscribed
        """
        Unsubscribed = 11

        """
        Contact complained to an e-mail
        """
        Complained = 12

        """
        Contact clicked an activation link
        """
        Activated = 20

        """
        Contact has opted to receive Transactional-only e-mails
        """
        TransactionalUnsubscribed = 21

        """
        Contact's status was changed manually
        """
        ManualStatusChange = 22

        """
        An Activation e-mail was sent
        """
        ActivationSent = 24

        """
        Contact was deleted
        """
        Deleted = 28

    """
    History of chosen Contact
    """
    class ContactHistory:
        """
        ID of history of selected Contact.
        """
        ContactHistoryID = None  # long

        """
        Type of event occured on this Contact.
        """
        EventType = None  # string

        """
        Numeric code of event occured on this Contact.
        """
        EventTypeValue = None  # ApiTypes.ContactHistEventType

        """
        Formatted date of event.
        """
        EventDate = None  # string

        """
        Name of selected channel.
        """
        ChannelName = None  # string

        """
        Name of template.
        """
        TemplateName = None  # string

        """
        IP Address of the event.
        """
        IPAddress = None  # string

        """
        Country of the event.
        """
        Country = None  # string

        """
        Information about the event
        """
        Data = None  # string

    """
    
    """
    class ContactSource(Enum):
        """
        Source of the contact is from sending an email via our SMTP or HTTP API's
        """
        DeliveryApi = 0

        """
        Contact was manually entered from the interface.
        """
        ManualInput = 1

        """
        Contact was uploaded via a file such as CSV.
        """
        FileUpload = 2

        """
        Contact was added from a public web form.
        """
        WebForm = 3

        """
        Contact was added from the contact api.
        """
        ContactApi = 4

    """
    
    """
    class ContactStatus(Enum):
        """
        Only transactional email can be sent to contacts with this status.
        """
        Transactional = -2

        """
        Contact has had an open or click in the last 6 months.
        """
        Engaged = -1

        """
        Contact is eligible to be sent to.
        """
        Active = 0

        """
        Contact has had a hard bounce and is no longer eligible to be sent to.
        """
        Bounced = 1

        """
        Contact has unsubscribed and is no longer eligible to be sent to.
        """
        Unsubscribed = 2

        """
        Contact has complained and is no longer eligible to be sent to.
        """
        Abuse = 3

        """
        Contact has not been activated or has been de-activated and is not eligible to be sent to.
        """
        Inactive = 4

        """
        Contact has not been opening emails for a long period of time and is not eligible to be sent to.
        """
        Stale = 5

        """
        Contact has not confirmed their double opt-in activation and is not eligible to be sent to.
        """
        NotConfirmed = 6

    """
    Number of Contacts, grouped by Status;
    """
    class ContactStatusCounts:
        """
        Number of engaged contacts
        """
        Engaged = None  # long

        """
        Number of active contacts
        """
        Active = None  # long

        """
        Number of complaint messages
        """
        Complaint = None  # long

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None  # long

        """
        Number of bounced messages
        """
        Bounced = None  # long

        """
        Number of inactive contacts
        """
        Inactive = None  # long

        """
        Number of transactional contacts
        """
        Transactional = None  # long

        """
        
        """
        Stale = None  # long

        """
        
        """
        NotConfirmed = None  # long

    """
    Number of Unsubscribed or Complaint Contacts, grouped by Unsubscribe Reason;
    """
    class ContactUnsubscribeReasonCounts:
        """

        """
        Unknown = None  # long

        """
        
        """
        NoLongerWant = None  # long

        """
        
        """
        IrrelevantContent = None  # long

        """
        
        """
        TooFrequent = None  # long

        """
        
        """
        NeverConsented = None  # long

        """
        
        """
        DeceptiveContent = None  # long

        """
        
        """
        AbuseReported = None  # long

        """
        
        """
        ThirdParty = None  # long

        """
        
        """
        ListUnsubscribe = None  # long

    """
    Type of credits
    """
    class CreditType(Enum):
        """
        Used to send emails.  One credit = one email.
        """
        Email = 9

        """
        Used to run a litmus test on a template.  1 credit = 1 test.
        """
        Litmus = 11

    """
    Daily summary of log status, based on specified date range.
    """
    class DailyLogStatusSummary:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # string

        """
        Proper email address.
        """
        Email = None  # int

        """
        Number of SMS
        """
        Sms = None  # int

        """
        Number of delivered messages
        """
        Delivered = None  # int

        """
        Number of opened messages
        """
        Opened = None  # int

        """
        Number of clicked messages
        """
        Clicked = None  # int

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None  # int

        """
        Number of complaint messages
        """
        Complaint = None  # int

        """
        Number of bounced messages
        """
        Bounced = None  # int

        """
        Number of inbound messages
        """
        Inbound = None  # int

        """
        Number of manually cancelled messages
        """
        ManualCancel = None  # int

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None  # int

    """
    Domain data, with information about domain records.
    """
    class DomainDetail:
        """
        Name of selected domain.
        """
        Domain = None  # string

        """
        True, if domain is used as default. Otherwise, false,
        """
        DefaultDomain = None  # bool

        """
        True, if SPF record is verified
        """
        Spf = None  # bool

        """
        True, if DKIM record is verified
        """
        Dkim = None  # bool

        """
        True, if MX record is verified
        """
        MX = None  # bool

        """
        
        """
        DMARC = None  # bool

        """
        True, if tracking CNAME record is verified
        """
        IsRewriteDomainValid = None  # bool

        """
        True, if verification is available
        """
        Verify = None  # bool

        """
        
        """
        Type = None  # ApiTypes.TrackingType

        """
        0 - NotValidated, 1 - Validated successfully, 2 - Invalid, 3 - Broken (tracking was frequnetly verfied in given period and still is invalid). For statuses: 0, 1, 3 tracking will be verified in normal periods. For status 2 tracking will be verified in high frequent periods.
        """
        TrackingStatus = None  # ApiTypes.TrackingValidationStatus

        """
        
        """
        CertificateStatus = None  # ApiTypes.CertificateValidationStatus

        """
        
        """
        CertificateValidationError = None  # string

        """
        
        """
        TrackingTypeUserRequest = None  # ApiTypes.TrackingType?

    """
    Detailed information about email credits
    """
    class EmailCredits:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # DateTime

        """
        Amount of money in transaction
        """
        Amount = None  # decimal

        """
        Source of URL of payment
        """
        Source = None  # string

        """
        Free form field of notes
        """
        Notes = None  # string

    """
    
    """
    class EmailJobFailedStatus:
        """

        """
        Address = None  # string

        """
        
        """
        Error = None  # string

        """
        RFC Error code
        """
        ErrorCode = None  # int

        """
        
        """
        Category = None  # string

    """
    
    """
    class EmailJobStatus:
        """
        ID number of your attachment
        """
        ID = None  # string

        """
        Name of status: submitted, complete, in_progress
        """
        Status = None  # string

        """
        
        """
        RecipientsCount = None  # int

        """
        
        """
        Failed = None  # List<ApiTypes.EmailJobFailedStatus>

        """
        Total emails sent.
        """
        FailedCount = None  # int

        """
        
        """
        Sent = None  # List<string>

        """
        Total emails sent.
        """
        SentCount = None  # int

        """
        Number of delivered messages
        """
        Delivered = None  # List<string>

        """
        
        """
        DeliveredCount = None  # int

        """
        
        """
        Pending = None  # List<string>

        """
        
        """
        PendingCount = None  # int

        """
        Number of opened messages
        """
        Opened = None  # List<string>

        """
        Total emails opened.
        """
        OpenedCount = None  # int

        """
        Number of clicked messages
        """
        Clicked = None  # List<string>

        """
        Total emails clicked
        """
        ClickedCount = None  # int

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None  # List<string>

        """
        Total emails clicked
        """
        UnsubscribedCount = None  # int

        """
        
        """
        AbuseReports = None  # List<string>

        """
        
        """
        AbuseReportsCount = None  # int

        """
        List of all MessageIDs for this job.
        """
        MessageIDs = None  # List<string>

    """
    
    """
    class EmailSend:
        """
        ID number of transaction
        """
        TransactionID = None  # string

        """
        Unique identifier for this email.
        """
        MessageID = None  # string

    """
    Status information of the specified email
    """
    class EmailStatus:
        """
        Email address this email was sent from.
        """
        From = None  # string

        """
        Email address this email was sent to.
        """
        To = None  # string

        """
        Date the email was submitted.
        """
        Date = None  # DateTime

        """
        Value of email's status
        """
        Status = None  # ApiTypes.LogJobStatus

        """
        Name of email's status
        """
        StatusName = None  # string

        """
        Date of last status change.
        """
        StatusChangeDate = None  # DateTime

        """
        Date when the email was sent
        """
        DateSent = None  # DateTime

        """
        Date when the email changed the status to 'opened'
        """
        DateOpened = None  # DateTime?

        """
        Date when the email changed the status to 'clicked'
        """
        DateClicked = None  # DateTime?

        """
        Detailed error or bounced message.
        """
        ErrorMessage = None  # string

        """
        ID number of transaction
        """
        TransactionID = None  # Guid

    """
    Email details formatted in json
    """
    class EmailView:
        """
        Body (text) of your message.
        """
        Body = None  # string

        """
        Default subject of email.
        """
        Subject = None  # string

        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None  # string

    """
    Encoding type for the email headers
    """
    class EncodingType(Enum):
        """
        Encoding of the email is provided by the sender and not altered.
        """
        UserProvided = -1

        """
        No endcoding is set for the email.
        """
        EENone = 0

        """
        Encoding of the email is in Raw7bit format.
        """
        Raw7bit = 1

        """
        Encoding of the email is in Raw8bit format.
        """
        Raw8bit = 2

        """
        Encoding of the email is in QuotedPrintable format.
        """
        QuotedPrintable = 3

        """
        Encoding of the email is in Base64 format.
        """
        Base64 = 4

        """
        Encoding of the email is in Uue format.
        """
        Uue = 5

    """
    Record of exported data from the system.
    """
    class Export:
        """

        """
        PublicExportID = None  # Guid

        """
        Date the export was created
        """
        DateAdded = None  # DateTime

        """
        Type of export
        """
        Type = None  # string

        """
        Current status of export
        """
        Status = None  # string

        """
        Long description of the export
        """
        Info = None  # string

        """
        Name of the file
        """
        Filename = None  # string

        """
        Link to download the export
        """
        Link = None  # string

    """
    Type of export
    """
    class ExportFileFormats(Enum):
        """
        Export in comma separated values format.
        """
        Csv = 1

        """
        Export in xml format
        """
        Xml = 2

        """
        Export in json format
        """
        Json = 3

    """
    
    """
    class ExportLink:
        """
        Direct URL to the exported file
        """
        Link = None  # string

    """
    Current status of export
    """
    class ExportStatus(Enum):
        """
        Export had an error and can not be downloaded.
        """
        Error = -1

        """
        Export is currently loading and can not be downloaded.
        """
        Loading = 0

        """
        Export is currently available for downloading.
        """
        Ready = 1

        """
        Export is no longer available for downloading.
        """
        Expired = 2

    """
    Number of Exports, grouped by export type
    """
    class ExportTypeCounts:
        """

        """
        Log = None  # long

        """
        
        """
        Contact = None  # long

        """
        Json representation of a campaign
        """
        Campaign = None  # long

        """
        True, if you have enabled link tracking. Otherwise, false
        """
        LinkTracking = None  # long

        """
        Json representation of a survey
        """
        Survey = None  # long

    """
    
    """
    class File:
        """
        Name of your file.
        """
        FileName = None  # string

        """
        Size of your attachment (in bytes).
        """
        Size = None  # int?

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None  # DateTime

        """
        When will the file be deleted from the system
        """
        ExpirationDate = None  # DateTime?

        """
        Unique ID of the file
        """
        FileID = None  # long

        """
        Content type of the file
        """
        ContentType = None  # string

    """
    
    """
    class IntervalType(Enum):
        """
        Daily overview
        """
        Summary = 0

        """
        Hourly, detailed information
        """
        Hourly = 1

    """
    Object containig tracking data.
    """
    class LinkTrackingDetails:
        """
        Number of items.
        """
        Count = None  # int

        """
        True, if there are more detailed data available. Otherwise, false
        """
        MoreAvailable = None  # bool

        """
        
        """
        TrackedLink = None  # List<ApiTypes.TrackedLink>

    """
    List of Lists, with detailed data about its contents.
    """
    class List:
        """
        ID number of selected list.
        """
        ListID = None  # int

        """
        Name of your list.
        """
        ListName = None  # string

        """
        Number of items.
        """
        Count = None  # int

        """
        ID code of list
        """
        PublicListID = None  # Guid?

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None  # DateTime

        """
        True: Allow unsubscribing from this list. Otherwise, false
        """
        AllowUnsubscribe = None  # bool

        """
        Query used for filtering.
        """
        Rule = None  # string

    """
    Detailed information about litmus credits
    """
    class LitmusCredits:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # DateTime

        """
        Amount of money in transaction
        """
        Amount = None  # decimal

    """
    Logs for selected date range
    """
    class Log:
        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None  # DateTime?

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None  # DateTime?

        """
        Number of recipients
        """
        Recipients = None  # List<ApiTypes.Recipient>

    """
    
    """
    class LogJobStatus(Enum):
        """
        All emails
        """
        All = 0

        """
        Email has been submitted successfully and is queued for sending.
        """
        ReadyToSend = 1

        """
        Email has soft bounced and is scheduled to retry.
        """
        WaitingToRetry = 2

        """
        Email is currently sending.
        """
        Sending = 3

        """
        Email has errored or bounced for some reason.
        """
        Error = 4

        """
        Email has been successfully delivered.
        """
        Sent = 5

        """
        Email has been opened by the recipient.
        """
        Opened = 6

        """
        Email has had at least one link clicked by the recipient.
        """
        Clicked = 7

        """
        Email has been unsubscribed by the recipient.
        """
        Unsubscribed = 8

        """
        Email has been complained about or marked as spam by the recipient.
        """
        AbuseReport = 9

    """
    Summary of log status, based on specified date range.
    """
    class LogStatusSummary:
        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None  # string

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None  # string

        """
        Overall duration
        """
        Duration = None  # double

        """
        Number of recipients
        """
        Recipients = None  # long

        """
        Number of emails
        """
        EmailTotal = None  # long

        """
        Number of SMS
        """
        SmsTotal = None  # long

        """
        Number of delivered messages
        """
        Delivered = None  # long

        """
        Number of bounced messages
        """
        Bounced = None  # long

        """
        Number of messages in progress
        """
        InProgress = None  # long

        """
        Number of opened messages
        """
        Opened = None  # long

        """
        Number of clicked messages
        """
        Clicked = None  # long

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None  # long

        """
        Number of complaint messages
        """
        Complaints = None  # long

        """
        Number of inbound messages
        """
        Inbound = None  # long

        """
        Number of manually cancelled messages
        """
        ManualCancel = None  # long

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None  # long

        """
        ID number of template used
        """
        TemplateChannel = None  # bool

    """
    Overall log summary information.
    """
    class LogSummary:
        """
        Summary of log status, based on specified date range.
        """
        LogStatusSummary = None  # ApiTypes.LogStatusSummary

        """
        Summary of bounced categories, based on specified date range.
        """
        BouncedCategorySummary = None  # ApiTypes.BouncedCategorySummary

        """
        Daily summary of log status, based on specified date range.
        """
        DailyLogStatusSummary = None  # List<ApiTypes.DailyLogStatusSummary>

    """
    
    """
    class MessageCategory(Enum):
        """

        """
        Unknown = 0

        """
        
        """
        Ignore = 1

        """
        Number of messages marked as SPAM
        """
        Spam = 2

        """
        Number of blacklisted messages
        """
        BlackListed = 3

        """
        Number of messages flagged with 'No Mailbox'
        """
        NoMailbox = 4

        """
        Number of messages flagged with 'Grey Listed'
        """
        GreyListed = 5

        """
        Number of messages flagged with 'Throttled'
        """
        Throttled = 6

        """
        Number of messages flagged with 'Timeout'
        """
        Timeout = 7

        """
        Number of messages flagged with 'Connection Problem'
        """
        ConnectionProblem = 8

        """
        Number of messages flagged with 'SPF Problem'
        """
        SPFProblem = 9

        """
        Number of messages flagged with 'Account Problem'
        """
        AccountProblem = 10

        """
        Number of messages flagged with 'DNS Problem'
        """
        DNSProblem = 11

        """
        
        """
        NotDeliveredCancelled = 12

        """
        Number of messages flagged with 'Code Error'
        """
        CodeError = 13

        """
        Number of manually cancelled messages
        """
        ManualCancel = 14

        """
        Number of messages flagged with 'Connection terminated'
        """
        ConnectionTerminated = 15

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = 16

    """
    Queue of notifications
    """
    class NotificationQueue:
        """
        Creation date.
        """
        DateCreated = None  # string

        """
        Date of last status change.
        """
        StatusChangeDate = None  # string

        """
        Actual status.
        """
        NewStatus = None  # string

        """
        
        """
        Reference = None  # string

        """
        Error message.
        """
        ErrorMessage = None  # string

        """
        Number of previous delivery attempts
        """
        RetryCount = None  # string

    """
    
    """
    class NotificationType(Enum):
        """
        Both, email and web, notifications
        """
        All = 0

        """
        Only email notifications
        """
        Email = 1

        """
        Only web notifications
        """
        Web = 2

    """
    Detailed information about existing money transfers.
    """
    class Payment:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # DateTime

        """
        Amount of money in transaction
        """
        Amount = None  # decimal

        """
        Source of URL of payment
        """
        Source = None  # string

    """
    Basic information about your profile
    """
    class Profile:
        """
        First name.
        """
        FirstName = None  # string

        """
        Last name.
        """
        LastName = None  # string

        """
        Company name.
        """
        Company = None  # string

        """
        First line of address.
        """
        Address1 = None  # string

        """
        Second line of address.
        """
        Address2 = None  # string

        """
        City.
        """
        City = None  # string

        """
        State or province.
        """
        State = None  # string

        """
        Zip/postal code.
        """
        Zip = None  # string

        """
        Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
        """
        CountryID = None  # int?

        """
        Phone number
        """
        Phone = None  # string

        """
        Proper email address.
        """
        Email = None  # string

        """
        Code used for tax purposes.
        """
        TaxCode = None  # string

    """
    
    """
    class QuestionType(Enum):
        """

        """
        RadioButtons = 1

        """
        
        """
        DropdownMenu = 2

        """
        
        """
        Checkboxes = 3

        """
        
        """
        LongAnswer = 4

        """
        
        """
        Textbox = 5

        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = 6

    """
    Detailed information about message recipient
    """
    class Recipient:
        """
        True, if message is SMS. Otherwise, false
        """
        IsSms = None  # bool

        """
        ID number of selected message.
        """
        MsgID = None  # string

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None  # string

        """
        Name of recipient's status: Submitted, ReadyToSend, WaitingToRetry, Sending, Bounced, Sent, Opened, Clicked, Unsubscribed, AbuseReport
        """
        Status = None  # string

        """
        Name of selected Channel.
        """
        Channel = None  # string

        """
        Creation date
        """
        Date = None  # string

        """
        Date when the email was sent
        """
        DateSent = None  # string

        """
        Date when the email changed the status to 'opened'
        """
        DateOpened = None  # string

        """
        Date when the email changed the status to 'clicked'
        """
        DateClicked = None  # string

        """
        Content of message, HTML encoded
        """
        Message = None  # string

        """
        True, if message category should be shown. Otherwise, false
        """
        ShowCategory = None  # bool

        """
        Name of message category
        """
        MessageCategory = None  # string

        """
        ID of message category
        """
        MessageCategoryID = None  # ApiTypes.MessageCategory

        """
        Date of last status change.
        """
        StatusChangeDate = None  # string

        """
        Date of next try
        """
        NextTryOn = None  # string

        """
        Default subject of email.
        """
        Subject = None  # string

        """
        Default From: email address.
        """
        FromEmail = None  # string

        """
        ID of certain mail job
        """
        JobID = None  # string

        """
        True, if message is a SMS and status is not yet confirmed. Otherwise, false
        """
        SmsUpdateRequired = None  # bool

        """
        Content of message
        """
        TextMessage = None  # string

        """
        Comma separated ID numbers of messages.
        """
        MessageSid = None  # string

        """
        Recipient's last bounce error because of which this e-mail was suppressed
        """
        ContactLastError = None  # string

    """
    Referral details for this account.
    """
    class Referral:
        """
        Current amount of dolars you have from referring.
        """
        CurrentReferralCredit = None  # decimal

        """
        Number of active referrals.
        """
        CurrentReferralCount = None  # long

    """
    Detailed sending reputation of your account.
    """
    class ReputationDetail:
        """
        Overall reputation impact, based on the most important factors.
        """
        Impact = None  # ApiTypes.ReputationImpact

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None  # double

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None  # double

        """
        
        """
        OpenedPercent = None  # double

        """
        
        """
        ClickedPercent = None  # double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None  # double

        """
        Percent of Bounced users
        """
        FailedSpamPercent = None  # double

        """
        Points from quantity of your emails.
        """
        RepEmailsSent = None  # double

        """
        Average reputation.
        """
        AverageReputation = None  # double

        """
        Actual price level.
        """
        PriceLevelReputation = None  # double

        """
        Reputation needed to change pricing.
        """
        NextPriceLevelReputation = None  # double

        """
        Amount of emails sent from this account
        """
        PriceLevel = None  # string

        """
        True, if tracking domain is correctly configured. Otherwise, false.
        """
        TrackingDomainValid = None  # bool

        """
        True, if sending domain is correctly configured. Otherwise, false.
        """
        SenderDomainValid = None  # bool

    """
    Reputation history of your account.
    """
    class ReputationHistory:
        """
        Creation date.
        """
        DateCreated = None  # string

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None  # double

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None  # double

        """
        
        """
        OpenedPercent = None  # double

        """
        
        """
        ClickedPercent = None  # double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None  # double

        """
        Points from proper setup of your account
        """
        SetupScore = None  # double

        """
        Points from quantity of your emails.
        """
        RepEmailsSent = None  # double

        """
        Numeric reputation
        """
        Reputation = None  # double

    """
    Overall reputation impact, based on the most important factors.
    """
    class ReputationImpact:
        """
        Abuses - mails sent to user without their consent
        """
        Abuse = None  # double

        """
        Users, that could not be reached.
        """
        UnknownUsers = None  # double

        """
        Number of opened messages
        """
        Opened = None  # double

        """
        Number of clicked messages
        """
        Clicked = None  # double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None  # double

        """
        Content analysis.
        """
        ServerFilter = None  # double

        """
        Tracking domain.
        """
        TrackingDomain = None  # double

        """
        Sending domain.
        """
        SenderDomain = None  # double

    """
    Information about Contact Segment, selected by RULE.
    """
    class Segment:
        """
        ID number of your segment.
        """
        SegmentID = None  # int

        """
        Filename
        """
        Name = None  # string

        """
        Query used for filtering.
        """
        Rule = None  # string

        """
        Number of items from last check.
        """
        LastCount = None  # long

        """
        History of segment information.
        """
        History = None  # List<ApiTypes.SegmentHistory>

    """
    Segment History
    """
    class SegmentHistory:
        """
        ID number of history.
        """
        SegmentHistoryID = None  # int

        """
        ID number of your segment.
        """
        SegmentID = None  # int

        """
        Date in YYYY-MM-DD format
        """
        Day = None  # int

        """
        Number of items.
        """
        Count = None  # long

        """
        
        """
        EngagedCount = None  # long

        """
        
        """
        ActiveCount = None  # long

        """
        
        """
        BouncedCount = None  # long

        """
        Total emails clicked
        """
        UnsubscribedCount = None  # long

        """
        
        """
        AbuseCount = None  # long

        """
        
        """
        InactiveCount = None  # long

    """
    
    """
    class SendingPermission(Enum):
        """
        Sending not allowed.
        """
        EENone = 0

        """
        Allow sending via SMTP only.
        """
        Smtp = 1

        """
        Allow sending via HTTP API only.
        """
        HttpApi = 2

        """
        Allow sending via SMTP and HTTP API.
        """
        SmtpAndHttpApi = 3

        """
        Allow sending via the website interface only.
        """
        Interface = 4

        """
        Allow sending via SMTP and the website interface.
        """
        SmtpAndInterface = 5

        """
        Allow sendnig via HTTP API and the website interface.
        """
        HttpApiAndInterface = 6

        """
        Sending allowed via SMTP, HTTP API and the website interface.
        """
        All = 255

    """
    Spam check of specified message.
    """
    class SpamCheck:
        """
        Total spam score from
        """
        TotalScore = None  # string

        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # string

        """
        Default subject of email.
        """
        Subject = None  # string

        """
        Default From: email address.
        """
        FromEmail = None  # string

        """
        ID number of selected message.
        """
        MsgID = None  # string

        """
        Name of selected channel.
        """
        ChannelName = None  # string

        """
        
        """
        Rules = None  # List<ApiTypes.SpamRule>

    """
    Single spam score
    """
    class SpamRule:
        """
        Spam score
        """
        Score = None  # string

        """
        Name of rule
        """
        Key = None  # string

        """
        Description of rule.
        """
        Description = None  # string

    """
    
    """
    class SplitOptimization(Enum):
        """
        Number of opened messages
        """
        Opened = 0

        """
        Number of clicked messages
        """
        Clicked = 1

    """
    Subaccount. Contains detailed data of your Subaccount.
    """
    class SubAccount:
        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None  # string

        """
        ApiKey that gives you access to our SMTP and HTTP API's.
        """
        ApiKey = None  # string

        """
        Proper email address.
        """
        Email = None  # string

        """
        ID number of mailer
        """
        MailerID = None  # string

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None  # string

        """
        Date of last activity on account
        """
        LastActivity = None  # string

        """
        Amount of email credits
        """
        EmailCredits = None  # string

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None  # bool

        """
        Amount of credits added to account automatically
        """
        MonthlyRefillCredits = None  # double

        """
        True, if account needs credits to buy templates. Otherwise, false
        """
        RequiresTemplateCredits = None  # bool

        """
        Amount of Litmus credits
        """
        LitmusCredits = None  # decimal

        """
        True, if account is able to send template tests to Litmus. Otherwise, false
        """
        EnableLitmusTest = None  # bool

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresLitmusCredits = None  # bool

        """
        True, if account can buy templates on its own. Otherwise, false
        """
        EnablePremiumTemplates = None  # bool

        """
        True, if account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None  # bool

        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None  # long

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None  # double

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None  # double

        """
        Percent of Bounced users
        """
        FailedSpamPercent = None  # double

        """
        Numeric reputation
        """
        Reputation = None  # double

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None  # long

        """
        Name of account's status: Deleted, Disabled, UnderReview, NoPaymentsAllowed, NeverSignedIn, Active, SystemPaused
        """
        Status = None  # string

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None  # int

        """
        Maximum number of contacts the account can have
        """
        MaxContacts = None  # int

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None  # bool

        """
        Sending permission setting for account
        """
        SendingPermission = None  # ApiTypes.SendingPermission

    """
    Detailed account settings.
    """
    class SubAccountSettings:
        """
        Proper email address.
        """
        Email = None  # string

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None  # bool

        """
        True, if account needs credits to buy templates. Otherwise, false
        """
        RequiresTemplateCredits = None  # bool

        """
        Amount of credits added to account automatically
        """
        MonthlyRefillCredits = None  # double

        """
        Amount of Litmus credits
        """
        LitmusCredits = None  # decimal

        """
        True, if account is able to send template tests to Litmus. Otherwise, false
        """
        EnableLitmusTest = None  # bool

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresLitmusCredits = None  # bool

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None  # int

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None  # int

        """
        Maximum number of contacts the account can have
        """
        MaxContacts = None  # int

        """
        True, if account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None  # bool

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None  # bool

        """
        Sending permission setting for account
        """
        SendingPermission = None  # ApiTypes.SendingPermission

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None  # string

        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None  # string

    """
    A survey object
    """
    class Survey:
        """
        Survey identifier
        """
        PublicSurveyID = None  # Guid

        """
        Creation date.
        """
        DateCreated = None  # DateTime

        """
        Last change date
        """
        DateUpdated = None  # DateTime?

        """
        
        """
        ExpiryDate = None  # DateTime?

        """
        Filename
        """
        Name = None  # string

        """
        Activate, delete, or pause your survey
        """
        Status = None  # ApiTypes.SurveyStatus

        """
        Number of results count
        """
        ResultCount = None  # int

        """
        
        """
        SurveySteps = None  # List<ApiTypes.SurveyStep>

        """
        URL of the survey
        """
        SurveyLink = None  # string

    """
    Object with the single answer's data
    """
    class SurveyResultAnswerInfo:
        """
        Answer's content
        """
        content = None  # string

        """
        Identifier of the step
        """
        surveystepid = None  # int

        """
        Identifier of the answer of the step
        """
        surveystepanswerid = None  # string

    """
    Single answer's data with user's specific info
    """
    class SurveyResultInfo:
        """
        Identifier of the result
        """
        SurveyResultID = None  # string

        """
        IP address
        """
        CreatedFromIP = None  # string

        """
        Completion date
        """
        DateCompleted = None  # DateTime

        """
        Start date
        """
        DateStart = None  # DateTime

        """
        Answers for the survey
        """
        SurveyResultAnswers = None  # List<ApiTypes.SurveyResultAnswerInfo>

    """
    
    """
    class SurveyResultsAnswer:
        """
        Identifier of the answer of the step
        """
        SurveyStepAnswerID = None  # string

        """
        Number of items.
        """
        Count = None  # int

        """
        Answer's content
        """
        Content = None  # string

    """
    Data on the survey's result
    """
    class SurveyResultsSummaryInfo:
        """
        Number of items.
        """
        Count = None  # int

        """
        Summary statistics
        """
        Summary = None  # Dictionary<int, ApiTypes.List`1>

    """
    
    """
    class SurveyStatus(Enum):
        """
        The survey is deleted
        """
        Deleted = -1

        """
        The survey is not receiving result for now
        """
        Expired = 0

        """
        The survey is active and receiving answers
        """
        Active = 1

    """
    Survey's single step info with the answers
    """
    class SurveyStep:
        """
        Identifier of the step
        """
        SurveyStepID = None  # int

        """
        Type of the step
        """
        SurveyStepType = None  # ApiTypes.SurveyStepType

        """
        Type of the question
        """
        QuestionType = None  # ApiTypes.QuestionType

        """
        Answer's content
        """
        Content = None  # string

        """
        Is the answer required
        """
        Required = None  # bool

        """
        Sequence of the answers
        """
        Sequence = None  # int

        """
        
        """
        SurveyStepAnswers = None  # List<ApiTypes.SurveyStepAnswer>

    """
    Single step's answer object
    """
    class SurveyStepAnswer:
        """
        Identifier of the answer of the step
        """
        SurveyStepAnswerID = None  # string

        """
        Answer's content
        """
        Content = None  # string

        """
        Sequence of the answers
        """
        Sequence = None  # int

    """
    
    """
    class SurveyStepType(Enum):
        """

        """
        PageBreak = 1

        """
        
        """
        Question = 2

        """
        
        """
        TextMedia = 3

        """
        
        """
        ConfirmationPage = 4

        """
        
        """
        ExpiredPage = 5

    """
    Template
    """
    class Template:
        """
        ID number of template.
        """
        TemplateID = None  # int

        """
        0 for API connections
        """
        TemplateType = None  # ApiTypes.TemplateType

        """
        Filename
        """
        Name = None  # string

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None  # DateTime

        """
        CSS style
        """
        Css = None  # string

        """
        Default subject of email.
        """
        Subject = None  # string

        """
        Default From: email address.
        """
        FromEmail = None  # string

        """
        Default From: name.
        """
        FromName = None  # string

        """
        HTML code of email (needs escaping).
        """
        BodyHtml = None  # string

        """
        Text body of email.
        """
        BodyText = None  # string

        """
        ID number of original template.
        """
        OriginalTemplateID = None  # int

        """
        Enum: 0 - private, 1 - public, 2 - mockup
        """
        TemplateScope = None  # ApiTypes.TemplateScope

    """
    List of templates (including drafts)
    """
    class TemplateList:
        """
        List of templates
        """
        Templates = None  # List<ApiTypes.Template>

        """
        List of draft templates
        """
        DraftTemplate = None  # List<ApiTypes.Template>

    """
    
    """
    class TemplateScope(Enum):
        """
        Template is available for this account only.
        """
        Private = 0

        """
        Template is available for this account and it's sub-accounts.
        """
        Public = 1

    """
    
    """
    class TemplateType(Enum):
        """
        Template supports any valid HTML
        """
        RawHTML = 0

        """
        Template is created and can only be modified in drag and drop editor
        """
        DragDropEditor = 1

    """
    Information about tracking link and its clicks.
    """
    class TrackedLink:
        """
        URL clicked
        """
        Link = None  # string

        """
        Number of clicks
        """
        Clicks = None  # string

        """
        Percent of clicks
        """
        Percent = None  # string

    """
    
    """
    class TrackingType(Enum):
        """

        """
        EENone = -2

        """
        
        """
        Delete = -1

        """
        
        """
        Http = 0

        """
        
        """
        ExternalHttps = 1

        """
        
        """
        InternalCertHttps = 2

        """
        
        """
        LetsEncryptCert = 3

    """
    Status of ValidDomain used by DomainValidationService to determine how often tracking validation should be performed.
    """
    class TrackingValidationStatus(Enum):
        """

        """
        Validated = 0

        """
        
        """
        NotValidated = 1

        """
        
        """
        Invalid = 2

        """
        
        """
        Broken = 3

    """
    Account usage
    """
    class Usage:
        """
        Proper email address.
        """
        Email = None  # string

        """
        True, if this account is a sub-account. Otherwise, false
        """
        IsSubAccount = None  # bool

        """
        
        """
        List = None  # List<ApiTypes.UsageData>

    """
    Detailed data about daily usage
    """
    class UsageData:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None  # DateTime

        """
        Number of finished tasks
        """
        JobCount = None  # int

        """
        Overall number of recipients
        """
        RecipientCount = None  # int

        """
        Number of inbound emails
        """
        InboundCount = None  # int

        """
        Number of attachments sent
        """
        AttachmentCount = None  # int

        """
        Size of attachments sent
        """
        AttachmentsSize = None  # long

        """
        Calculated cost of sending
        """
        Cost = None  # decimal

        """
        Number of pricate IPs
        """
        PrivateIPCount = None  # int?

        """
        
        """
        PrivateIPCost = None  # decimal

        """
        Number of SMS
        """
        SmsCount = None  # int?

        """
        Overall cost of SMS
        """
        SmsCost = None  # decimal

        """
        Cost of templates
        """
        TemplateCost = None  # decimal

        """
        Cost of email credits
        """
        EmailCreditsCost = None  # int?

        """
        Cost of template credit
        """
        TemplateCreditsCost = None  # int?

        """
        Cost of litmus credits
        """
        LitmusCost = None  # decimal

        """
        Cost of 1 litmus credit
        """
        LitmusCreditsCost = None  # decimal

        """
        Daily cost of Contact Delivery Tools
        """
        ContactCost = None  # decimal

        """
        Number of contacts
        """
        ContactCount = None  # long

        """
        
        """
        SupportCost = None  # decimal

        """
        
        """
        EmailCost = None  # decimal
