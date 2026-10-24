# Chest Math

Event bazaar apricot chest, week, cost and time arithmetic. The 265 apricots at 14 apricots a chest take 19 chests, the last chest holding 13 apricots.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The chests truth** - the apricots (1 to 1000000) divided by the apricots a chest (1 to 1000), rounded up, with what the last chest holds.
- **The weeks truth** - the apricots divided by the apricots used a week (1 to 100000), with the apricots left for the next week.
- **The cost truth** - the chests (1 to 100000) times the chest price ($0.01 to $999.99) to the cent, and spread over the apricots, half rounded up.
- **The time truth** - the apricots divided by the apricots packed a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any apricot, chest or venue and does not know whether apricots will really stay fresh, a supplier will run out or a price will hold, and it gives no verdict that a chest is worth its price or an apricot is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every chest recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
