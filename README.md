# Uncertainty Propagation

I made these scripts to help me speed up my physics homework. Doing error propagation by hand for every single measurement is really slow, so I’m automating it.

## The Theory

To calculate the uncertainty ($\delta V$), I'm using the **partial derivative method**. Since the volume depends on multiple measured values, the total error is the sum of the partial derivatives with respect to each variable, multiplied by that variable's own uncertainty.

### 1. Hollow Cylinder (Tube)
The formula for the volume is:
$$V = \frac{1}{4} \pi (D^2 - d^2)h$$

To find the error formula, I derived $V$ for each variable ($h, D, d$):
* $\frac{\partial V}{\partial h} = \frac{\pi}{4}(D^2 - d^2)$
* $\frac{\partial V}{\partial D} = \frac{\pi}{2}Dh$
* $\frac{\partial V}{\partial d} = -\frac{\pi}{2}dh$

Putting it all together (and taking the absolute values):
$$\delta V = \frac{\pi}{4} [2h(D \cdot \delta D + d \cdot \delta d) + (D^2 - d^2)\delta h]$$

### 2. Sphere
For a sphere using the diameter ($D$):
$$V = \frac{1}{6} \pi D^3$$

The derivative is much simpler here:
$$\delta V = \frac{d V}{d D} \delta D = \frac{1}{6} \pi (3D^2) \delta D$$

## How to use
1. Run the script with Python.
2. Input the measurements (mean value) and the instrument uncertainty ($\delta$) when asked.
3. The script prints out the result as `Volume +- Uncertainty`.
4. Type `y` to calculate another measure or `n` to quit.