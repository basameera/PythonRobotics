# Bayes Filter

[Ref. 1](#reference)

## Visualization project

[Ref. 2](#reference)

## Automatic sensor model estimate (ASME)

**TODO**

- [ ] Need to learn how `norm.fit()` work -> maximum likelihood

Automatic sensor modeling flow:
1. Move to a random position in space
2. Take 200 samples (dataset)
3. Using `norm.fit()` to estimate mu, std
4. Do steps 1. to 3. for two more different random positions in space. (Now there's three mu values and std values)
5. Get the avg. of all std values as the model parameter
6. using this `std`, do `norm.fit()` again to refine the mu estimates.

### To Do

* PDF as bar plot
* Motion model
* Mesurement model
* Main window
* Key press plot
* Main window handling class
* B. F. calculations
* draw boat

### Reference

1. Bayes Filter Youtube (https://www.youtube.com/watch?v=6uEgLv1Mr2s)
2. The Two Stages of Bayes Filtering (https://www.youtube.com/watch?v=Qa8YMP9dQYo)
3. Bayesian Filtering Review (https://www.youtube.com/watch?v=rlp4uaVNHVM)

To watch

1. Introduction to Bayesian statistics, part 1: The basic concepts (https://www.youtube.com/watch?v=0F0QoMCSKJ4)
