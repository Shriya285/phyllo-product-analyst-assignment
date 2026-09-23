# Candidate pack

Meridian is a made-up company. The API is not live, so there is nothing to call
and no key to request. Treat these files as if they were captured from a real
integration.

```
API_DOCS.md    the published documentation
responses/     three payloads captured from the API
ticket.md      one customer complaint
```

Each response file is named for the request that produced it:

| File | Request | Status returned |
|------|---------|-----------------|
| `orders_page1.json` | `GET /v1/orders` | `200` |
| `orders_page2.json` | `GET /v1/orders?starting_after=cur_8f2a19bd` | `200` |
| `order_ord_9999.json` | `GET /v1/orders/ord_9999` (no such order) | `200` |
