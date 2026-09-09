# explain-ci demo

A deliberately failing test suite used to demo
[explain-ci](https://github.com/gopalcnepal/explain-ci).

`inventory.py` has a boundary-condition bug: `items_to_restock` is documented
to return items **at or below** the restock threshold, but it compares with
`<` instead of `<=`, so an item sitting exactly on the threshold is missed.

Opening a PR runs the suite, `test_items_exactly_at_threshold_are_restocked`
fails, and explain-ci posts the explanation as a PR comment.
