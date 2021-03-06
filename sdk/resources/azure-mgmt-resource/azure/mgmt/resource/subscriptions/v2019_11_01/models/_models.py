# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Location(Model):
    """Location information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar name: The location name.
    :vartype name: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    :ivar regional_display_name: The display name of the location and its
     region.
    :vartype regional_display_name: str
    :param metadata: Metadata of the location, such as lat/long, paired
     region, and others.
    :type metadata:
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.LocationMetadata
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'regional_display_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'regional_display_name': {'key': 'regionalDisplayName', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'LocationMetadata'},
    }

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.name = None
        self.display_name = None
        self.regional_display_name = None
        self.metadata = kwargs.get('metadata', None)


class LocationMetadata(Model):
    """Location metadata information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar region_type: The type of the region. Possible values include:
     'Physical', 'Logical'
    :vartype region_type: str or
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.RegionType
    :ivar region_category: The category of the region. Possible values
     include: 'Recommended', 'Other'
    :vartype region_category: str or
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.RegionCategory
    :ivar geography_group: The geography group of the location.
    :vartype geography_group: str
    :ivar longitude: The longitude of the location.
    :vartype longitude: str
    :ivar latitude: The latitude of the location.
    :vartype latitude: str
    :ivar physical_location: The physical location of the Azure location.
    :vartype physical_location: str
    :param paired_region: The regions paired to this region.
    :type paired_region:
     list[~azure.mgmt.resource.subscriptions.v2019_11_01.models.PairedRegion]
    """

    _validation = {
        'region_type': {'readonly': True},
        'region_category': {'readonly': True},
        'geography_group': {'readonly': True},
        'longitude': {'readonly': True},
        'latitude': {'readonly': True},
        'physical_location': {'readonly': True},
    }

    _attribute_map = {
        'region_type': {'key': 'regionType', 'type': 'str'},
        'region_category': {'key': 'regionCategory', 'type': 'str'},
        'geography_group': {'key': 'geographyGroup', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'physical_location': {'key': 'physicalLocation', 'type': 'str'},
        'paired_region': {'key': 'pairedRegion', 'type': '[PairedRegion]'},
    }

    def __init__(self, **kwargs):
        super(LocationMetadata, self).__init__(**kwargs)
        self.region_type = None
        self.region_category = None
        self.geography_group = None
        self.longitude = None
        self.latitude = None
        self.physical_location = None
        self.paired_region = kwargs.get('paired_region', None)


class ManagedByTenant(Model):
    """Information about a tenant managing the subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar tenant_id: The tenant ID of the managing tenant. This is a GUID.
    :vartype tenant_id: str
    """

    _validation = {
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManagedByTenant, self).__init__(**kwargs)
        self.tenant_id = None


class Operation(Model):
    """Microsoft.Resources operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display:
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Resources
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile,
     endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class PairedRegion(Model):
    """Information regarding paired region.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the paired region.
    :vartype name: str
    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PairedRegion, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.subscription_id = None


class Subscription(Model):
    """Subscription information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID for the subscription. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar display_name: The subscription display name.
    :vartype display_name: str
    :ivar tenant_id: The subscription tenant ID.
    :vartype tenant_id: str
    :ivar state: The subscription state. Possible values are Enabled, Warned,
     PastDue, Disabled, and Deleted. Possible values include: 'Enabled',
     'Warned', 'PastDue', 'Disabled', 'Deleted'
    :vartype state: str or
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.SubscriptionState
    :param subscription_policies: The subscription policies.
    :type subscription_policies:
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.SubscriptionPolicies
    :param authorization_source: The authorization source of the request.
     Valid values are one or more combinations of Legacy, RoleBased, Bypassed,
     Direct and Management. For example, 'Legacy, RoleBased'.
    :type authorization_source: str
    :param managed_by_tenants: An array containing the tenants managing the
     subscription.
    :type managed_by_tenants:
     list[~azure.mgmt.resource.subscriptions.v2019_11_01.models.ManagedByTenant]
    :param tags: The tags attached to the subscription.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'display_name': {'readonly': True},
        'tenant_id': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'SubscriptionState'},
        'subscription_policies': {'key': 'subscriptionPolicies', 'type': 'SubscriptionPolicies'},
        'authorization_source': {'key': 'authorizationSource', 'type': 'str'},
        'managed_by_tenants': {'key': 'managedByTenants', 'type': '[ManagedByTenant]'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Subscription, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.display_name = None
        self.tenant_id = None
        self.state = None
        self.subscription_policies = kwargs.get('subscription_policies', None)
        self.authorization_source = kwargs.get('authorization_source', None)
        self.managed_by_tenants = kwargs.get('managed_by_tenants', None)
        self.tags = kwargs.get('tags', None)


class SubscriptionPolicies(Model):
    """Subscription policies.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location_placement_id: The subscription location placement ID. The
     ID indicates which regions are visible for a subscription. For example, a
     subscription with a location placement Id of Public_2014-09-01 has access
     to Azure public regions.
    :vartype location_placement_id: str
    :ivar quota_id: The subscription quota ID.
    :vartype quota_id: str
    :ivar spending_limit: The subscription spending limit. Possible values
     include: 'On', 'Off', 'CurrentPeriodOff'
    :vartype spending_limit: str or
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.SpendingLimit
    """

    _validation = {
        'location_placement_id': {'readonly': True},
        'quota_id': {'readonly': True},
        'spending_limit': {'readonly': True},
    }

    _attribute_map = {
        'location_placement_id': {'key': 'locationPlacementId', 'type': 'str'},
        'quota_id': {'key': 'quotaId', 'type': 'str'},
        'spending_limit': {'key': 'spendingLimit', 'type': 'SpendingLimit'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionPolicies, self).__init__(**kwargs)
        self.location_placement_id = None
        self.quota_id = None
        self.spending_limit = None


class TenantIdDescription(Model):
    """Tenant Id information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the tenant. For example,
     /tenants/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar tenant_id: The tenant ID. For example,
     00000000-0000-0000-0000-000000000000.
    :vartype tenant_id: str
    :ivar tenant_category: Category of the tenant. Possible values include:
     'Home', 'ProjectedBy', 'ManagedBy'
    :vartype tenant_category: str or
     ~azure.mgmt.resource.subscriptions.v2019_11_01.models.TenantCategory
    :ivar country: Country/region name of the address for the tenant.
    :vartype country: str
    :ivar country_code: Country/region abbreviation for the tenant.
    :vartype country_code: str
    :ivar display_name: The display name of the tenant.
    :vartype display_name: str
    :ivar domains: The list of domains for the tenant.
    :vartype domains: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'tenant_category': {'readonly': True},
        'country': {'readonly': True},
        'country_code': {'readonly': True},
        'display_name': {'readonly': True},
        'domains': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'tenant_category': {'key': 'tenantCategory', 'type': 'TenantCategory'},
        'country': {'key': 'country', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'domains': {'key': 'domains', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(TenantIdDescription, self).__init__(**kwargs)
        self.id = None
        self.tenant_id = None
        self.tenant_category = None
        self.country = None
        self.country_code = None
        self.display_name = None
        self.domains = None
