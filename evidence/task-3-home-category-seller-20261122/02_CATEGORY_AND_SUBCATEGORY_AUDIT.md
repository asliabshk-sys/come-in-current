# Report 2 — Category and Subcategory Audit

## Current structure

The customer `CATEGORIES` constant in `frontend/src/data/catalog.ts` is a **flat 17-item list**, not a main-category/subcategory tree:

`atta-rice-dal`, `masalas-oils`, `snacks`, `bakery`, `beverages`, `tea-coffee`, `dairy-breakfast`, `fruits`, `fruits-veggies`, `personal-care`, `household`, `frozen-foods`, `packaged-foods`, `eggs`, `stationery`, `baby-care`, `pet-supplies`.

`categories.tsx`, Home and `category/[slug].tsx` navigate by stable ID. Seller product suggestions and the product editor use the same IDs; `ShopIn.category_ids` accepts a list for shop discovery.

## Backend/data rules

- `ProductIn.category_id` is required (`backend/server.py`, ProductIn); no server-owned category collection/hierarchy was found in inspected scope.
- Product/category mapping is persisted per product in `products.category_id`; `GET /catalog/products` returns eligible products of approved shops.
- Medical/pharmacy and stationery tokens are explicitly **directory-only**; server rejects online product creation/update for them (`server.py` around `_reject_directory_only_product`).
- Focused tests passed: catalog, shopping and directory-only category contracts were included in the **84 PASS** Task 3 selection.

## Classification and recommendation for owner discussion only

| Finding | Classification | Recommendation (not implemented) |
|---|---|---|
| Grocery items split across many flat launch tiles | IMPLEMENTED BUT NOT VERIFIED | Consider a limited launch taxonomy: Grocery & Staples; Fruits & Vegetables; Kitchen & Household; Stationery & Books as directory-only. Keep Restaurant Mode separate. |
| `fruits` and `fruits-veggies` | PARTIALLY OVERLAPPING | Decide whether to retain distinct Fruits/Vegetables children under a future parent; do not merge existing IDs without migration/mapping plan. |
| `stationery` | IMPLEMENTED & VERIFIED | Keep directory-only unless owner separately changes commerce policy. |
| Subcategory hierarchy | NOT IMPLEMENTED | Current structure is flat IDs; no safe reorganization was attempted. |
| Product mapping | IMPLEMENTED & VERIFIED | `category_id` flows from seller/product/import to public catalog; no mapping changed. |

No category was deleted, renamed, moved or remapped in Task 3.
