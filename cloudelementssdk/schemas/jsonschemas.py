string_schema = {
    'type': 'string',
    'maxLength': 255,
    'minLength': 1,
    'blank': False,
    'required': False
}

string_schema_required  = {
    'type': 'string',
    'maxLength': 255,
    'minLength': 1,
    'blank': False,
    'required': True
}

boolean_schema = {
    'type': 'boolean',
    'required': False
}

monetary_schema = {
    'type': 'integer',
    'minimum': 0,
    'required': False
}
create_lead_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'FirstName': string_schema,
        'LastName': string_schema,
        'Phone': string_schema,
        'Description': string_schema,
        'LeadSource': string_schema,
        'Title': string_schema,
        'Email': string_schema,
        'Company': string_schema,
        'Rating': string_schema,
        'PostalCode': string_schema,
        'Salutation': string_schema,
        'Industry': string_schema,
        'Street': string_schema,
        'Status': string_schema,
        'IsUnreadByOwner':  boolean_schema,
        'City': string_schema,
        'State': string_schema,
        'Country': string_schema,
        'Fax': string_schema,
        'AnnualRevenue':  monetary_schema
      }
}

contact_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'Phone': string_schema,
        'Email': string_schema,
        'FirstName': string_schema,
        'LastName': string_schema_required,
        'Department': string_schema,
        'MobilePhone': string_schema,
        'Title': string_schema,
        'LastModifiedDate': string_schema,
        'AccountId': string_schema,
        'LastReferencedDate': string_schema,
        'Salutation': string_schema,
        'Name': string_schema,
        'CreatedById': string_schema,
        'OwnerId': string_schema,
        'PhotoUrl': string_schema,
        'IsDeleted': string_schema,
        'IsEmailBounced': string_schema,
        'HasOptedOutOfEmail': string_schema,
        'LastViewedDate': string_schema,
        'Birthdate': string_schema,
        'SystemModStamp': string_schema,
        'LeadSource': string_schema,
        'CreatedDate': string_schema,
        'Fax': string_schema,
        'LastModifiedById': string_schema,
        'MailingStreet': string_schema
    }
}

account_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
          "Name": string_schema_required,
          "Website": string_schema,
          "Phone": string_schema,
          "BillingStreet": string_schema,
          "BillingCity": string_schema,
          "BillingState": string_schema,
          "BillingPostalCode": string_schema,
          "BillingCountry": string_schema,
          "Type": string_schema,
          "AnnualRevenue": monetary_schema,
          "NumberOfEmployees": monetary_schema,
          "Description": string_schema,
          "ShippingStreet": string_schema,
          "AccountNumber": string_schema,
          "Fax": string_schema,
          "Rating": string_schema,
          "Ownership": string_schema,
          "Sic": string_schema,
          "Industry":  string_schema
        }
}
