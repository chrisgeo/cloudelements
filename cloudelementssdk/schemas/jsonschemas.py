string_schema = {
    'type': 'string',
    'maxLength': 255,
    'minLength': 1,
    'blank': False,
    'required': False
}

string_schema_allow_empty = {
    'type': 'string',
    'maxLength': 255,
    'blank': True,
    'required': False
}

array_of_strings_schema =  {
    'type': 'array',
    'uniqueItems': True,
    'items': [
        string_schema
    ],
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

integer_schema = {
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
        'AnnualRevenue':  integer_schema
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
lead_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        "FirstName": string_schema,
        "LastName": string_schema_required,
        "Phone": string_schema,
        "Description": string_schema,
        "LeadSource": string_schema,
        "Title": string_schema,
        "Email": string_schema,
        "Company": string_schema,
        "Rating": string_schema,
        "PostalCode": string_schema,
        "Salutation": string_schema,
        "Industry": string_schema,
        "Street": string_schema,
        "Status": string_schema,
        "IsUnreadByOwner": boolean_schema,
        "City": string_schema,
        "State": string_schema,
        "Country": string_schema,
        "Fax": string_schema,
        "AnnualRevenue": integer_schema
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
          "AnnualRevenue": integer_schema,
          "NumberOfEmployees": integer_schema,
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

instance_key_schema = {
    'enum': ['sfdc', 'sugar'],
    'required': False
}

instance_element_schema = {
    'type': 'object',
    'properties': {
            'id': integer_schema,
            'name': string_schema,
            'createdDate': integer_schema,
            'updatedDate': integer_schema,
            'key': instance_key_schema,
            'description': string_schema,
            'active': boolean_schema,
            'deleted': boolean_schema,
            'typeOauth': boolean_schema,
            'trialAccount': boolean_schema,
            'trialAccountDescription': string_schema,
            'existingAccountDescription': string_schema,
            'configDescription':  string_schema,
            'signupURL': string_schema,
            'authenticationType': string_schema,
            'hub': string_schema,
            'transformationsEnabled': boolean_schema
          }
}

instance_provision_schema = {
    "type": "object",
    "properties": {
        "maxCacheSize": integer_schema,
        "element":  instance_element_schema,
        "providerData": {
            "type": "object",
            "properties": {
                "code": string_schema,
            },
            'required': False
        },
        "configuration": {
            "type": 'object',
            'properties': {
                "oauth.callback.url": string_schema,
                "oauth.api.key": string_schema,
                "oauth.api.secret": string_schema
            },
            'required': False
        },
        "tags": string_schema_allow_empty,
        "name": string_schema,
        "valid": boolean_schema,
        "channelName": string_schema,
        "updatedDate": integer_schema,
        "id": integer_schema,
        "cacheTimeToLive": integer_schema,
        "token": string_schema,
        "description": string_schema,
        "cachingEnabled": boolean_schema,
        "createdDate": integer_schema,
        "disabled": boolean_schema
    }
}
