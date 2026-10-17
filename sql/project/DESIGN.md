# Database Design: Personal Expense Management

#### Video Demo: https://youtu.be/WnkfrpyOKEY

#### Description:
This is the final project for Harvard's CS50's Introduction to databases with SQL (CS50SQL). This project is a store manager online system, written entirely in SQL. It allows store owners to track inventory, analyze customer purchase history, and manage the status of each order effectively, thereby optimizing operations and improving customer experience.

---
## Scope

**In-Scope:**
* Manage customer accounts: The system allows storing customers personal information. Each customer has a unique account to track cart and purchase history.
* Manage store items: The system allows adding, updating, deleting items information.
* Manage transactions: Add information transaction after buying items. Each account may many transactions, each transaction may have many items.
* Manage items rate: Store item reviews. Each account only rate one type of item once.
* Manage cart: Store items added to temporary cart.
* Query data: Provides predefined VIEWS for easy querying of important information such as detailed transaction history, summary of transactions for the day, and total value of each invoice.

**Out-of-Scope:**
* Payment: Only payment method, not integrated with any payment gateways.
* Shipping Management: No detailed tracking of shipping process (tracking code, shipping unit).
* Authentication and security: Passwords are stored in text, not hashed.

## Entities and Relationships

Our database consists of six main entities: `accounts`, `items`, `carts`, `rates`, `transactions`, `transactions_detail`

1.  **`accounts`**: Stores information about customers.
    * `id`: Primary key, unique identifier for each account.
    * `name`: Account name. (PHAN VAN BAC, ...)
    * `password`: Account password. (hashed string)
    * `email`: Account email.
    * `phone`: Account phone.
    * `address`: Account address.
    * `created_date`: Account created date.

2.  **`items`**: Store information about items.
    * `id`: Primary key, unique identifier for each item.
    * `name`: Item name (Shirts, Pants, ...).
    * `description`: A short text that summarizes the item.
    * `price`: Price of item (Positive and can change depend on market).
    * `inventory_quantity`: Number of items in inventory.

3. **`carts`**: Store items that customer may be buy.
    * `account_id`, `item_id`: Composite primary Key, each customers can add many item in their cart.
    * `quantity`: Number of items added to cart.

4. **`rates`**: Store reviews of customers about items.
    * `account_id`, `item_id`: Composite primary key, each customers only rate one item once.
    * `comment`: A short text of customer that review about item.
    * `rate`: A integer of customer that review about quality item. (In range from 1 to 5)

5.  **`transactions`**: Records all activities of customers.
    * `id`: Primary key, unique identifier for each transaction.
    * `account_id`: Indicates who the transaction is from.
    * `transaction_date`: Date of occurrence transaction.
    * `payment_method`: The method the user prefers to pay. (Cash On Delivery - COD, Quick Response Code - QR, E-wallet)
    * `state`: The state of transaction. ("processing", "canceled", "delivered")

6.  **`transactions_detail`**: Describe detail about transactions.
    * `id`: Primary key.
    * `transaction_id`: Indicate which transaction this information is for.
    * `item_id`: Indicates the item included in the transaction.
    * `quantity`: Number of items buy.
    * `current_price`: Price of item at the current time.

## Entity Relationship Diagram (ERD)

![ERD STORE MANAGER ONLINE](erd_store_manager.png)

## Optimizations

**Indexes**: To speed up frequent filtering and reporting queries

1. **Table: `accounts`**
    * `idx_accounts_cover`: On column `(name, phone, email)`to speed up customer information search.

2. **Table: `items`**
    * `idx_items_cover`: On column `(price, name)` to speed up searching for items by price.

3. **Table: `rates`**
    * `idx_rates`: On column `rate` to speed up searching for reviews by rate.

4. **Table: `transactions`**
    * `idx_transactions`: On column `transaction_date` to speed up searching for transactions in day.
    * `idx_transactions_cover`: On column `(account_id, transaction_date)` to speed up searching for a customer's transactions on a specific date.

5. **Table: `transactions_detail`**
    * `idx_transactions_detail_cover`: On column `(item_id, transaction_id)` to speed up searching for items in a transaction.

**Views**: Simplify querying complex and frequently requested reports.
1. **`cart_detail`**: Display details of the items in each user's shopping cart.
2. **`transaction_history`**: Display details about transactions.
3. **`rate_detail`**: Display details about reviews of each customer for each item.
4. **`total_bill`**: Display total amount of a transaction.

## Limitations

**Security**:
* Passwords only store characters, while encryption must go through application logic.

**Data Integrity & Business Logic:**
* Simple state management: Not bound at the database level but must depend entirely on the application logic.
* No division of roles.
* Lack of Race Condition: The system does not have a mechanism to handle the case where multiple users buy the same last item in stock at the same time. This can lead to overselling (inventory_quantity can be negative) or cause errors.

**Functionility:**
* The system only records transaction payments, while financial transactions are conducted through payment gateways.
* The system does not record the history of changes to items in inventory.
* No shipping tracking function
