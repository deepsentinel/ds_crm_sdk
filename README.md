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

```python
data, status_code = client.get_account(account_id='123')
print(data, status_code)
```

---

#### 2. `get_accounts_by_filters(...) -> tuple`
Retrieve accounts by applying filters.
- **filters**:
  - `email_address` (optional): Filter accounts by email address using a fuzzy search (i.e., checks if the email contains the given value).
  - `phone_number` (optional): Filter accounts by phone number (should be exact match).
  - `parent_account_id` (optional): Filter accounts by parent account ID.
  - `account_type_id` (optional): Filter accounts by account type ID.
- **Additional Parameters**:
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).

**Note:** The `filters` parameter is a dictionary that can include any of the above fields. Multiple filters are not supported in a single request.
```python
filters = {'email_address': 'xyz@abc.com'}
data, status_code = client.get_accounts_by_filters(filters=filters)
print(data, status_code)
```

---

#### 3. `get_account_addresses(...) -> tuple`
Retrieve addresses for a specific account.
- **Parameters**:
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).
** Note: ** The `filters` parameter is a dictionary that can include any of the above fields. Multiple filters are not supported in a single request.
```python
data, status_code = client.get_account_addresses(account_id='123')
print(data, status_code)
```

---

#### 4. `get_account_addresses_by_filters(...) -> tuple`
Retrieve addresses for a specific account by applying filters.
- **filters**:
  - `address_type` (optional): Filter by address type (`shipping` or `billing`).
  - `is_default` (optional): Filter by default status (`true` or `false`).
- **Additional Parameters**:
  - `account_id`: ID of the account to retrieve addresses for.
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).
```python
filters = {'address_type': 'shipping'}
data, status_code = client.get_account_addresses_by_filters(account_id='123',
                                                            filters=filters)
print(data, status_code)
```

---

#### 5. `get_account_types(...) -> tuple`
Retrieve all account types.
- **Parameters** :
  - `offset` (optional): Start point for the pagination.
  - `limit` (optional): Maximum number of records (default: 10).
  - `sort_by` (optional): Field to sort by (default: `created`).
  - `sort_order` (optional): Sort order (`asc` or `desc`, default: `desc`).
```python
data, status_code = client.get_account_types()
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
├── endpoints/           # Enum definitions for CRM endpoints
├── client.py            # CRMClient & AsyncCRMClient
└── models.py            # Common pydantic models
```

---

## 🛠️ Extending the SDK

- Add new payload logic: subclass `PayloadBuilder`
- Add new transport (e.g., MQ/gRPC): subclass `Transport` or `AsyncTransport`
- Register new builders using the factory registry

---
