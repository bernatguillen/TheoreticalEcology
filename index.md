---
layout: page
title: Notes
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Theoretical Ecology

## Simon A. Levin

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
* Constant fitnesses [^1]
* Random mating.
* One locus (genotypes only at one place).
* Diploid population.
* Two alleles (two forms of a gene: *A/B* or *A/a*). Combination is order-independent

Probabilities: 2 alleles \\(A,a\\), proportions: \\(p\\), \\(q=1-p\\). A new zygote will be:

\\(AA\to p^2\\), after fitness selection \\(AA\to p^2 W_{AA}\\).\\
\\(Aa\to 2pq\\), after fitness selection \\(Aa\to 2pq W_{Aa}\\).\\
\\(aa\to q^2\\), after fitness selection \\(aa\to q^2 W_{aa}\\).

If all fitnesses were 1 (no selection), the gene frequency doesn't change in the next pool (if we pick an individual at random and then a gene at random):
\\(P[A] = 1\cdot p^2 + \frac{2pq}{2} + 0\cdot q^2 = p\\).

If there is fitness involved:

Mean fitness: \\(\bar{W} = p^2 W_{AA} + 2pqW_{Aa} + q^2 W_{aa}\\). The mean fitness of each allele is:

\\(W_A = pW_{AA} + qW_{Aa}\\)

\\(W_a = pW_{Aa} + qW_{aa}\\)

Note that \\(\bar{W} = pW_A + qW_a\\).

What is the gene frequency after selection? [^2]

$$
\begin{align*}
  & p'=P[\to A] = \frac{1\cdot p^2 W_{AA} + 0.5 \cdot 2pqW_{Aa} + 0 \cdot q^2W_{aa}}{\bar{W}} = \\
  & p\cdot \frac{pW_{AA} + qW_{Aa}}{\bar{W}} = p\cdot \frac{W_A}{\bar{W}}
\end{align*}
$$

Similarly:

$$q'=P[\to a] = q\cdot \frac{W_a}{\bar{W}}$$

Cases:\\
\\(W_{AA} > W_{Aa} > W_{aa}\\)\\
![Case 1]({{ baseurl }}/TheoreticalEcology/Images/WAA0.7WAa0.2Waa0.1.png "Case 1")

\\(W_{AA} < W_{Aa} < W_{aa}\\)\\
![Case 2]({{ baseurl }}/TheoreticalEcology/Images/WAA0.1WAa0.2Waa0.7.png "Case 2")

\\(W_{AA} < W_{Aa} > W_{aa}\\): Equilibrium\\
![Case 3: Equilibrium]({{ baseurl }}/TheoreticalEcology/Images/WAA0.3WAa1.0Waa0.3.png "Case 3")

\\(W_{AA} > W_{Aa} < W_{aa}\\): Disruptive Selection\\
![Case 4: Disruptive selection]({{ baseurl }}/TheoreticalEcology/Images/WAA0.9WAa0.5Waa0.9.png "Case 4")

## Day 2

Differences between adaptation and optimization.

* Adaptation: Process of gradual improvement. It is the adjustment to current conditions, conditions may change and you may never actually get to an end point. It may reach a local optimum but not global.
* Optimization: Outcome

The problem is that the decisions may affect the landscape (e.g. an optimal environment will attract so many individuals that the environment may become worse).

When we talk about the average fitness of the members of a population it may not be the fitness of the group. Selection of the best individuals may not mean the best possible strategy/situation for the group. Related concepts: Common Pool Resources, Public Goods.[^3] An example in our own bodies is cancer, it's a breakdown of public good. Another problem of Public Goods and cancer is that tumor cells have to produce cytocides (?).

The mapping from genotype to phenotype is not one to one. Some people say "put aside genotype constraints, ask how could we do it with a phenotypic strategy?". Of course there are genetic constraints, but this phenotypic approach revolutionizes evolutionary ecology. For next day read (Hamilton and May) on dispersal.

Going back to last day: \\(p = [A]\\) is the frequency of allele A, \\(q = 1-p\\) the frequency of allele a. \\(p' = p\frac{W_A}{\bar{W}}\\). \\(\bar{W}\\) in the disruptive selection case will never reach an unstable equilibrium. Disruptive selection may help in creating what's called symphatic speciation.

Let's look at how \\(p\\) changes.
$$\Delta p = p' - p = p(\frac{W_A}{\bar{W}}-1) = pq\frac{W_A-W_a}{\bar{W}}$$

Note that \\(pq\\) is a measure of the variation of the initial population. And we can think of \\(\frac{W_A-W_a}{\bar{W}}\\) as a measure of selective differences[^4]. Note that \\(W_A, W_a\\) depend on \\(p,q\\), so the process of adaptation will lead to equilibrium where we eliminate all genetic variation or reach the point where it doesn't matter what allele you have (balance polymorphisms).

Important: We have to find ways to maintain genetic variation. Evolution has found ways to do it:
* Mutation (which leads to genetic drifts), the mutation rate is a parameter that is subject to adaptability: For example Influenza A mutates at a great rate to adapt to rapidly changing environment. But you don't want too high rate because you may miss local optima.
* Recombination (sexual or other) is an important way in which nature generates genetic variation.

Trade-off between exploration and exploitation. Example: Companies that keep exploring/innovating may drive the changing environment.

Let's look at the changing rate of \\(\bar{W}\\): \\(\frac{\partial\bar{W}}{\partial p} = 2pW_{AA} + (2-4p)W_{Aa} + 2(p-1)W_{aa}\\). \\
We can simplify: \\(\frac{1}{2}\frac{\partial\bar{W}}{\partial p} = pW_{AA} + (1-2p)W_{Aa} + (p-1)W_{aa}\\). \\
Finally, regrouping terms: \\(\frac{1}{2}\frac{\partial\bar{W}}{\partial p} = pW_{AA}+(1-p)W_{Aa} - (pW_{Aa} + (1-p)W_{aa}) = W_A - Wa\\).

Therefore, \\(\Delta p = \frac{pq}{2} \frac{\bar{W}_p}{\bar{W}}\\). Note that this is \\(\frac{\Delta p}{\Delta t}\\) but \\(\Delta t\\) is large (1 generation).

If we consider the long run, and look at the increment in short periods of time this approximates the time derivative of \\(p\\). Thus,
\\(\frac{dp}{dt} \approx \frac{pq}{2}\frac{\bar{W}_p}{\bar{W}}\\) and finally,
$$\frac{d\bar{W}}{dt} = \frac{d\bar{W}}{dp}\frac{dp}{dt} = \frac{pq}{2}\frac{(\bar{W}_p)^2}{\bar{W}}$$

#### Coevolution

Lewington (paper we have to read) was the first to formalize the game theoretical part of coevolution, and argued for minimax strategies but there really is not a lot of support for that.

Game: Suppose we want to auction off a hundred dollars. Every player bids and the highest bidder wins (paying what they bid), but the second highest bidder has to pay as well. This is a frequency depending situation, fitnesses are not constants, the strategy will keep escalating. In behavioral ecology there's a similar concept: war of attrition. Each encounter is a way of measuring the strength of opponent. Would you retire if you think your opponent is stronger? (no, you can still bluff, and you can assume the opponent will tire before you). There is no optimal fixed strategy for the game (there is mixed strategy).

Another interesting game: Bet on 2/3 of the average of what everybody else chooses (keynesian contest). If all players are rational (nash eq.) then 0 would be the solution. In general if you keep taking steps taking into account what other players will do you will keep going down.[^5]

A third game: Prisoner's dilemma. If players are rational, the optimal strategy is to defect. But, if both cooperate both are better off.

#### Hawk Dove interaction

If two doves interact, each gets \\(0.5V\\). If a dove and a hawk interact, the hawk gets it \\(1V\\). If the two Hawks interact, then they fight, but get less than they would if they cooperated.

Insert table:

H-H: \\(\frac{V-C}{2}\\)
H-D: \\(V\\)
D-H: \\(0\\)
D-D: \\(\frac{V}{2}\\)

Cases: \\(V > C\\), it's better to be a hawk. \\(V<C\\), there will be an oscillation in the repeated game which might reach an equilibrium. [insert plot]
[^1]: Fitness depends on survivability and reproductive power. Density/Frequency dependence
[^2]: Idea: relative fitness of receiving allele A from parent affects new frequency
[^3]: N.S.: (Bernat) I think Elinor Ostrom is a good read for this.
[^4]: If I know I got A from my parent and my sibling got a from their parent, who of us is better of?
[^5]: N.S.: (Bernat) I think the distribution of k-step thinkers is a Poisson distribution with parameter around 2. So some people will just bid randomly, some more will assume everybody bids randomly so will bid on 33 (2/3*50), most of the people will assume everybody will bid on 33 and will bid on 22, and then less people will assume that and will bid on 14, even less will bid on 6, less on 4, etc.
