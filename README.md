## Deep Sentinel CRM SDK

A client SDK for communicating with a CRM service, currently supporting:

- ✅ Client-specific payload builders using **Pydantic**
- ✅ Both **sync** and **async** transports
- ✅ Full support for HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- ✅ Configurable headers and token-based auth
- ✅ Clean, extensible architecture [Modularized for easy extension]

---

## 📦 Install

```bash
pip install .
```

---

## 🚀 Usage

### 🔹 Synchronous Client

* CRMClient Init

```python
from ds_crm_sdk.http_clients.crm_client import CRMClient
from ds_crm_sdk.payloads import MainPayloadBuilder
from ds_crm_sdk.transports import DSHTTPTransport
from ds_crm_sdk.constants import ClientOrigin

builder = MainPayloadBuilder()
transport = DSHTTPTransport(token_provider=lambda: 'fake-token')
base_url = '<<domain base url>>'
client = CRMClient(client_origin=ClientOrigin.EWAP, builder=builder,
                   base_url=base_url, transport=transport)
```

#### 1. `get_account(account_id: str) -> tuple`
Retrieve account details by account ID.
- **Parameters**:
  - `account_id`: ID of the account to retrieve.
```python
data, status_code = client.get_account(account_id='123')
print(data, status_code)
```

---

#### 2. `get_accounts(...) -> tuple`
Retrieve accounts by applying filters.
- **filters**:
  - `email` (optional): Filter accounts by email address using a fuzzy search (i.e., checks if the email contains the given value).
  - `phone` (optional): Filter accounts by phone number (should be exact match).
  - `parent_account_id` (optional): Filter accounts by parent account ID.
  - `type_id` (optional): Filter accounts by account type ID.
- **Additional Parameters**:
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).

**Note:** The `filters` parameter is a dictionary that can include any of the above fields. Multiple filters are supported, all should match to retrieve the result.
```python
filters = {'email': 'xyz@abc.com'}
data, status_code = client.get_accounts_by_filters(filters=filters, offset=0, limit=10, sort_by='created', sort_order='asc')
print(data, status_code)
```

---

#### 3. `get_account_addresses(...) -> tuple`
Retrieve addresses for a specific account.
- **filters**:
  - `address_type` (optional): Filter by address type (`shipping` or `billing`).
  - `need_only_default` (optional): Filter by default address type (`true` or `false`). Example: address_type=shipping and need_only_default=true will return only the default shipping address.
- **Parameters**:
  - `account_id`: ID of the account to retrieve addresses for.
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).
** Note: ** The `filters` parameter is a dictionary that can include any of the above fields. Multiple filters are not supported in a single request. Only one filter can be applied at a time.
```python
filters = {'address_type': 'shipping', 'need_only_default': 'true'}
data, status_code = client.get_account_addresses(account_id='123', filters=filters, offset=0, limit=10,
                                                 sort_by='created', sort_order='asc')
print(data, status_code)
```

---
#### 4. `get_account_address_by_id(...) -> tuple`
Retrieve a specific address for an account by address ID.
- **Parameters**:
  - `account_id`: ID of the account to retrieve address for.
  - `address_id`: ID of the address to retrieve.
```python
data, status_code = client.get_account_address_by_id(account_id='123', address_id='456')
```
---

#### 5. `get_account_types(...) -> tuple`
Retrieve all account types.
- **filters**:
  - `name` (optional): Filter account types by name using a fuzzy search.
  - `type_id` (optional): Filter account types by ID.
- **Parameters** :
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).
** Note: ** The `filters` parameter is a dictionary that can include any of the above fields. Multiple filters are supported, all should match to retrieve the result.
```python
filters = {'name': 'Business'}
data, status_code = client.get_account_types(filters=filters, offset=0, limit=10, sort_by='created', sort_order='asc')
print(data, status_code)
```

---

#### 5. `get_account_type(...) -> tuple`
Retrieve all account types.
- **Parameters** :
    - `type_id`: ID of the account type to retrieve.
```python
data, status_code = client.get_account_type(type_id='789')
print(data, status_code)
```
---

### 🔹 Asynchronous Client
* Note: Ensure crmClient is initialized with `AsyncCRMClient` and `AsyncTransport`. Api calls can be awaited.
* Should return the same data as the synchronous client.

---

## 📦 Project Structure

```text
crm_sdk/
├── transports/          # Sync and async HTTP transport classes
├── payloads/            # Client-specific payload builders
├── http_clients/        # Asynchronous and synchronous client implementations, along with common client logic
├── constants/           # Constants and enums used across the SDK
```

---

## 🛠️ Extending the SDK

- Add new payload logic: subclass `PayloadBuilder`
- Add new transport (e.g., MQ/gRPC): subclass `Transport` or `AsyncTransport`
- Register new builders using the factory registry

---
