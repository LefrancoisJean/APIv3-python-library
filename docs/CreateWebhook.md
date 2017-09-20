# CreateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the webhook | 
**description** | **str** | Description of the webhook | [optional] 
**events** | **list[str]** | Events triggering the webhook. Possible values for Transactional type webhook – request, delivered, hardBounce, softBounce, blocked, spam, invalid, deferred, click, opened, uniqueOpened and unsubscribed and possible values for Marketing type webhook – spam, opened, click, hardBounce, softBounce, unsubscribed, listAddition &amp; delivered | [optional] 
**type** | **str** | Type of the webhook | [optional] [default to 'transactional']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

