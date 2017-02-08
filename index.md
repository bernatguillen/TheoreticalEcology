# Theoretical Ecology
## Simon A. Levin
Notes curated and maintained by Bernat Guillen
## Day 1

### Models
A model is defined by Current state -> Next State (infer rules) -> Long periods -> asymptotic
There are three kinds of models: Predictive, Understanding, Managerial.

### Evolution and Optimization
People think about evolution as a process of improvement. The first formal approach to this idea is Fisher's landscape / Adaptive landscape. For each genotype we associate a fitness, the idea is that evolution tends to optimize on the fitness.

#### Fisher's fundamental theorem:
Assumptions:

* No immigration/emigration
* No mutation
* Large population (ignore stochastic effects)
* Constant fitnesses ^[Fitness depends on survivability and reproductive power. Density/Frequency dependence]
* Random mating.
* One locus (genotypes only at one place).
* Diploid population.
* Two alleles (two forms of a gene: *A/B* or *A/a*). Combination is order-independent

Probabilities: 2 alleles $A,a$, proportions: $p$, $q=1-p$. A new zygote will be:

$AA\to p^2$, after fitness selection $AA\to p^2 W_{AA}$.
$Aa\to 2pq$, after fitness selection $Aa\to 2pq W_{Aa}$.
$aa\to q^2$, after fitness selection $aa\to q^2 W_{aa}$.


If all fitnesses were 1 (no selection), the gene frequency doesn't change in the next pool (if we pick an individual at random and then a gene at random):
$P[A] = 1\cdot p^2 + \frac{2pq}{2} + 0\cdot q^2 = p$.

If there is fitness involved:

Mean fitness: $\bar{W} = p^2 W_{AA} + 2pqW_{Aa} + q^2 W_{aa}$. The mean fitness of each alleles are:

$W_A = pW_{AA} + qW_{Aa}$

$W_a = pW_{Aa} + qW_{aa}$

Note that $\bar{W} = pW_A + qW_a$.

What is the gene frequency after selection? ^[Idea: relative fitness of receiving allele A from parent affects new frequency]

$$p'=P[\to A] = \frac{1\cdot p^2 W_{AA} + 0.5 \cdot 2pqW_{Aa} + 0 \cdot q^2W_{aa}}{\bar{W}} = p\cdot \frac{pW_{AA} + qW_{Aa}}{\bar{W}} = p\cdot \frac{W_A}{\bar{W}}$$

Similarly:

$$q'=P[\to a] = q\cdot \frac{W_a}{\bar{W}}$$

Cases (Insert plots):
$W_{AA} > W_{Aa} > W_{aa}$
![case1](/Images/WAA0.7WAa0.2Waa0.1.png "Case 1")
$W_{AA} < W_{Aa} < W_{aa}$
![case2](/Images/WAA0.1WAa0.2Waa0.7.png "Case 2")
$W_{AA} < W_{Aa} > W_{aa}$: Equilibrium
![case3](/Images/WAA0.3WAa1.0Waa0.3.png "Case 3")
$W_{AA} > W_{Aa} < W_{aa}$: Disruptive Selection
![case4](/Images/WAA0.9WAa0.5Waa0.9.png "Case 4")
