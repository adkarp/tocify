# Weekly ToC Digest (week of 2026-02-16)

> Three papers address advanced plasma simulation methods (tensor networks, discrete gradients, PIC schemes) with scores 0.76–0.77, directly supporting computational plasma modeling. Five tokamak/fusion papers (scores 0.61–0.78) cover MHD instabilities, confinement, and magnetized physics core to propulsion design. Remaining papers span rare-event sampling, quantum methods, and materials processing with minimal thruster relevance. This batch lacks papers directly targeting MHD, plasma propulsion, or scientific machine learning (SciML). The highest-scoring item (0.68) addresses aerospace optimal control but is disconnected from magnetohydrodynamic effects. Several papers explore agentic LLM systems (scores 0.42–0.62), which marginally align with R&D acceleration workflows but lack domain specificity in physics simulation or thruster design. Two papers directly relevant to agentic R&D pipelines: perceptual self-reflection in physics simulation code generation (0.88) and OptiML framework for CUDA kernel synthesis (0.76). One moderately relevant agentic architecture overview on skill-equipped LLM agents (0.72). Majority of batch comprises general-purpose AI/ML papers (NLP, vision, finance, e-commerce, medical imaging) with minimal or zero relevance to MHD, plasma propulsion, or computational physics. Top-ranked papers feature SciML methods (PINNs, Gaussian processes) and RL-driven design synthesis applicable to MHD optimization and agentic R&D acceleration. Most remaining items lac

**Included:** 40 (score ≥ 0.35)  
**Scored:** 199 total items

---

## [Perceptual Self-Reflection in Agentic Physics Simulation Code Generation](https://arxiv.org/abs/2602.12311)
*[ArXiv] Artificial Intelligence*  
Score: **0.88**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Physics-Simulation, Code-Generation, SciML

Multi-agent framework for automated physics simulation code generation with self-reflection mechanisms aligns directly with agentic R&D pipelines and scientific code acceleration.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12311v1 Announce Type: cross Abstract: We present a multi-agent framework for generating physics simulation code from natural language descriptions, featuring a novel perceptual self-reflection mechanism for validation. The system employs four specialized agents: a natural language interpreter that converts user requests into physics-based descriptions; a technical requirements generator that produces scaled simulation parameters; a physics code generator with automated self-correctio…

</div>
</details>

---

## [Variability of MHD Instabilities in Benign Termination of High-Current Runaway Electron Beams in the JET and DIII-D Tokamaks](https://arxiv.org/abs/2601.02262)
*[ArXiv] Plasma Physics*  
Score: **0.78**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Tokamak, Instabilities

MHD instabilities in tokamak physics directly inform plasma confinement and control strategies relevant to magnetohydrodynamic propulsion systems and plasma dynamics.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2601.02262v2 Announce Type: replace Abstract: Benign termination, in which magnetohydrodynamic (MHD) instabilities deconfine runaway electrons (REs) following hydrogenic injections, is a promising strategy for mitigating dangerous RE loads after disruptions. Recent experiments on the Joint European Torus (JET) have explored this scenario at higher pre-disruptive plasma currents than are achievable on other devices, revealing challenges in obtaining benign terminations at $I_p \geq 2.5$ MA.…

</div>
</details>

---

## [Tensor Network Compression for Fully Spectral Vlasov-Poisson Simulation](https://arxiv.org/abs/2602.13092)
*[ArXiv] Plasma Physics*  
Score: **0.77**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Plasma, Numerical Methods, Kinetic Simulation

Advanced numerical methods for kinetic plasma simulation using tensor networks and spectral approaches; applicable to efficient plasma solver development for propulsion modeling.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13092v1 Announce Type: cross Abstract: We propose a numerical method for kinetic plasma simulation in which the phase-space distribution function is represented by a low-rank tensor network with an adaptive level of compression. The Vlasov-Poisson system is advanced using Strang splitting, and each substep is treated spectrally in the corresponding variable. By expressing both the distribution function and the Fourier transform as tensor network objects (state and operator representat…

</div>
</details>

---

## [Tensor Network Compression for Fully Spectral Vlasov-Poisson Simulation](https://arxiv.org/abs/2602.13092)
*[ArXiv] Computational Physics*  
Score: **0.77**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Plasma, Numerical Methods, Kinetic Simulation

Advanced numerical methods for kinetic plasma simulation using tensor networks and spectral approaches; applicable to efficient plasma solver development for propulsion modeling.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13092v1 Announce Type: new Abstract: We propose a numerical method for kinetic plasma simulation in which the phase-space distribution function is represented by a low-rank tensor network with an adaptive level of compression. The Vlasov-Poisson system is advanced using Strang splitting, and each substep is treated spectrally in the corresponding variable. By expressing both the distribution function and the Fourier transform as tensor network objects (state and operator representatio…

</div>
</details>

---

## [Structure preservation using discrete gradients in the Vlasov-Poisson-Landau system](https://arxiv.org/abs/2602.13068)
*[ArXiv] Plasma Physics*  
Score: **0.76**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Plasma, Numerical Methods, PIC, Conservation

Structure-preserving PIC scheme with conservation laws for hot plasma kinetics; directly applicable to accurate plasma simulation for thruster physics.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13068v1 Announce Type: new Abstract: We present a novel structure-preserving framework for solving the Vlasov-Poisson-Landau system of equations using a particle in cell (PIC) discretization combined with discrete gradient time integrators. The Vlasov-Poisson-Landau system is an accurate model for studying hot plasma dynamics at a kinetic scale where small-angle Coulomb collisions dominate. Our scheme guarantees conservation of mass, momentum and energy as well as preservation of the …

</div>
</details>

---

## [OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305)
*[ArXiv] Artificial Intelligence*  
Score: **0.76**  
Published: 2026-02-16T05:00:00+00:00
Tags: Computational-Optimization, Program-Synthesis, GPU-Computing

Automated synthesis and optimization of high-performance CUDA kernels via systematic exploration mirrors agentic acceleration of computational research, relevant for MHD simulation performance.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12305v1 Announce Type: cross Abstract: Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language in…

</div>
</details>

---

## [A Machine Learning Approach to the Nirenberg Problem](https://arxiv.org/abs/2602.12368)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.76**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, PINN, Computational-Physics, Differential-Equations

PINNs for differential geometry problems demonstrate SciML methods applicable to non-Euclidean geometric computations in plasma domains; mesh-free approach relevant to adaptive computational methods.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12368v1 Announce Type: new Abstract: This work introduces the Nirenberg Neural Network: a numerical approach to the Nirenberg problem of prescribing Gaussian curvature on $S^2$ for metrics that are pointwise conformal to the round metric. Our mesh-free physics-informed neural network (PINN) approach directly parametrises the conformal factor globally and is trained with a geometry-aware loss enforcing the curvature equation. Additional consistency checks were performed via the Gauss-B…

</div>
</details>

---

## [A Machine Learning Approach to the Nirenberg Problem](https://arxiv.org/abs/2602.12368)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.76**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, PINN, Inverse-Problems, Geometry

PINNs for differential geometry; applicable to solving geometric inverse problems in plasma confinement and magnetic field topology.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12390v1 Announce Type: new Abstract: We study neural networks with trainable low-degree rational activation functions and show that they are more expressive and parameter-efficient than modern piecewise-linear and smooth activations such as ELU, LeakyReLU, LogSigmoid, PReLU, ReLU, SELU, CELU, Sigmoid, SiLU, Mish, Softplus, Tanh, Softmin, Softmax, and LogSoftmax. For an error target of $\varepsilon>0$, we establish approximation-theoretic separations: Any network built from standard fi…

</div>
</details>

---

## [Physics-Informed Transformer operator for the prediction of three-dimensional turbulence](https://arxiv.org/abs/2601.19351)
*[ArXiv] Fluid Dynamics*  
Score: **0.76**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Physics-Informed, Turbulence, Neural-Operators

Combines physics-informed neural operators (Transformer-based) with 3D turbulence prediction, demonstrating SciML techniques applicable to complex fluid dynamics. Relevant to computational methods for high-fidelity plasma and fluid simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2601.19351v4 Announce Type: replace Abstract: Data-driven turbulence prediction methods often face challenges related to data dependency and lack of physical interpretability. In this paper, we propose a physics-informed Transformer operator (PITO) and its implicit variant (PIITO) for predicting three-dimensional (3D) turbulence, which are developed based on the vision Transformer (ViT) architecture with an appropriate patch size. Given the current flow field, the Transformer operator comp…

</div>
</details>

---

## [Long-Pulse Fast Ignition in MagLIF](https://arxiv.org/abs/2602.12673)
*[ArXiv] Plasma Physics*  
Score: **0.75**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Fusion, High-Energy-Density

Magnetized liner inertial fusion (MagLIF) employs magnetic confinement and high-energy-density plasma physics, relevant to understanding MHD effects and pulsed propulsion concepts.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12673v1 Announce Type: new Abstract: The fast ignition paradigm for inertial confinement fusion (ICF) allows for extremely high gains but requires fuel to be heated very quickly to outpace hotspot disassembly and energy losses. This demands lasers with high power and intensity, posing engineering challenges that have called into question the fundamental practicality of fast ignition. Magnetized liner inertial fusion (MagLIF) circumvents these problems through its large-aspect-ratio cy…

</div>
</details>

---

## [Quantitative 3D non-linear simulations of shattered pellet injection in ASDEX Upgrade using JOREK](https://arxiv.org/abs/2602.12813)
*[ArXiv] Plasma Physics*  
Score: **0.74**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Simulation, Tokamak

3D non-linear MHD simulations of plasma control in tokamaks; demonstrates advanced computational MHD techniques relevant to plasma dynamics and control.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12813v1 Announce Type: new Abstract: Shattered pellet injection (SPI) as primary mitigation method for major disruptions in ITER has a large parameter space available for optimization including the total amount of injected material, the size of the individual pellet fragments, the material composition, and the timing of multiple injections. This flexibility needs to be exploited to simultaneously minimize thermal heat loads, electromagnetic vessel forces, and formation of relativistic…

</div>
</details>

---

## [Exact moment models for conservation laws in phase space](https://arxiv.org/abs/2602.13180)
*[ArXiv] Plasma Physics*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Plasma, Moment Models, Computational Physics

Moment-based models reduce kinetic simulation complexity while capturing essential physics; useful for efficient multiscale plasma modeling in propulsion contexts.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13180v1 Announce Type: new Abstract: Moment equations offer a compelling alternative to the kinetic description of plasmas, gases, and liquids. Their simulation requires fewer degrees of freedom than phase space models, yet it can still incorporate kinetic effects to a certain extent. To derive moment equations, we use a parameterization of the distribution function using centered moments, as proposed by Burby. This yields moment equations for which the parameterized distribution func…

</div>
</details>

---

## [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
*[ArXiv] Artificial Intelligence*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, LLM-Architecture, R&D-Automation

Comprehensive framework for modular skill-equipped agents and dynamic capability extension relevant to building agentic R&D pipelines for scientific discovery workflows.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12430v1 Announce Type: cross Abstract: The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure,…

</div>
</details>

---

## [OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Optimization, Computational

Addresses automated program synthesis and performance optimization via LLM-guided exploration—relevant to agentic R&D pipelines for computational physics simulations where kernel tuning is critical.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12305v1 Announce Type: cross Abstract: Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language in…

</div>
</details>

---

## [Latent-space variational data assimilation in two-dimensional turbulence](https://arxiv.org/abs/2512.15470)
*[ArXiv] Fluid Dynamics*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: Data-Assimilation, Variational-Methods, Turbulence, Inverse-Problems

Demonstrates latent-space variational methods for inverse problems in turbulent flows, employing reduced-order modeling techniques. Applicable to accelerating computational workflows in MHD and plasma simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2512.15470v2 Announce Type: replace Abstract: Starting from limited measurements of a turbulent flow, data assimilation (DA) attempts to estimate all the spatio-temporal scales of motion. Success is dependent on whether the system is observable from the measurements, or how much of the initial turbulent field is encoded in the available measurements. Adjoint-variational DA minimises the discrepancy between the true and estimated measurements by optimising the initial velocity or vorticity …

</div>
</details>

---

## [Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081)
*[ArXiv] Robotics*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Robotics, Control

Directly addresses agentic workflows for automated control through language model planning and skill selection. Relevant to R&D acceleration via agent-based task execution and reasoning loops.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13081v1 Announce Type: new Abstract: Recent work leverages the capabilities and commonsense priors of generative models for robot control. In this paper, we present an agentic control system in which a reasoning-capable language model plans and executes tasks by selecting and invoking robot skills within an iterative planner and executor loop. We deploy the system on two physical robot platforms in two settings: (i) tabletop grasping, placement, and box insertion in indoor mobile mani…

</div>
</details>

---

## [An Oscillation-Free Real Fluid Quasi-Conservative Finite Volume Method for Transcritical and Phase-Change Flows](https://arxiv.org/abs/2602.00658)
*[ArXiv] Fluid Dynamics*  
Score: **0.71**  
Published: 2026-02-16T05:00:00+00:00
Tags: Finite-Volume, Real-Fluids, Numerical-Methods, Phase-Change

Presents advanced finite volume methods for real-fluid dynamics with shock-capturing, relevant to high-energy-density plasma simulations and propellant modeling in thruster environments.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.00658v2 Announce Type: replace-cross Abstract: A new Real Fluid Quasi-Conservative (RFQC) finite volume method is developed to address the numerical simulation of real fluids involving shock waves in transcritical and phase-change flows. To eliminate the spurious pressure oscillations inherent in fully conservative schemes, we extend the classic quasi-conservative method, originally designed for two-phase flows, to real fluids governed by arbitrary equations of state (EoS). The RFQC m…

</div>
</details>

---

## [Roadmap for warm dense matter physics](https://arxiv.org/abs/2505.02494)
*[ArXiv] Plasma Physics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, High-Energy-Density, Computational Physics

Comprehensive overview of strongly coupled plasma physics and computational methods; relevant to understanding non-ideal effects in high-density plasma regimes.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2505.02494v2 Announce Type: replace Abstract: This roadmap presents the state-of-the-art, current challenges and near future developments anticipated in the thriving field of warm dense matter physics. Originating from strongly coupled plasma physics, high pressure physics and high energy density science, the warm dense matter physics community has recently taken a giant leap forward. This is due to spectacular developments in laser technology, diagnostic capabilities, and computer simulat…

</div>
</details>

---

## [Optimal Take-off under Fuzzy Clearances](https://arxiv.org/abs/2602.13166)
*[ArXiv] Artificial Intelligence*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Aerospace, Optimal Control, Unmanned Aircraft, Fuzzy Logic

Addresses optimal control under uncertainty and adaptive constraint handling for unmanned aircraft; relevant to aerospace R&D acceleration and decision-making systems, though not directly focused on MHD or plasma propulsion.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13166v1 Announce Type: new Abstract: This paper presents a hybrid obstacle avoidance architecture that integrates Optimal Control under clearance with a Fuzzy Rule Based System (FRBS) to enable adaptive constraint handling for unmanned aircraft. Motivated by the limitations of classical optimal control under uncertainty and the need for interpretable decision making in safety critical aviation systems, we design a three stage Takagi Sugeno Kang fuzzy layer that modulates constraint ra…

</div>
</details>

---

## [AstRL: Analog and Mixed-Signal Circuit Synthesis with Deep Reinforcement Learning](https://arxiv.org/abs/2602.12402)
*[ArXiv] Artificial Intelligence*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Reinforcement-Learning, Circuit-Design, Optimization

Applies RL to automated circuit design optimization across non-differentiable design spaces, demonstrating agentic approaches to complex engineering synthesis problems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12402v1 Announce Type: cross Abstract: Analog and mixed-signal (AMS) integrated circuits (ICs) lie at the core of modern computing and communications systems. However, despite the continued rise in design complexity, advances in AMS automation remain limited. This reflects the central challenge in developing a generalized optimization method applicable across diverse circuit design spaces, many of which are distinct, constrained, and non-differentiable. To address this, our work casts…

</div>
</details>

---

## [Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/abs/2602.12342)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Reinforcement-Learning, Long-Horizon-Planning

RL-based agent with language models for long-horizon reasoning; relevant to agentic R&D automation for iterative physics simulations and design optimization.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12342v1 Announce Type: new Abstract: How can we train agents to navigate uncertainty over long horizons? In this work, we propose {\Delta}Belief-RL, which leverages a language model's own intrinsic beliefs to reward intermediate progress. Our method utilizes the change in the probability an agent assigns to the target solution for credit assignment. By training on synthetic interaction data, {\Delta}Belief-RL teaches information-seeking capabilities that consistently outperform purely…

</div>
</details>

---

## [MASPRM: Multi-Agent System Process Reward Model](https://arxiv.org/abs/2510.24803)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, RL, MCTS

Develops process-level reward models for multi-agent inference guidance, applicable to agentic scientific workflows where sequential decision-making and computational budgeting are essential.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2510.24803v2 Announce Type: replace Abstract: Practical deployment of multi-agent systems (MAS) demands strong performance at test time, motivating methods that guide search during inference and selectively spend compute to improve quality. We present the Multi-Agent System Process Reward Model (MASPRM). It assigns values to partial inter-agent transcripts for each action and each agent, and acts as a controller during inference. MASPRM is trained from multi-agent Monte Carlo Tree Search (…

</div>
</details>

---

## [A Corrected Open Boundary Framework for Lattice Boltzmann Immiscible Pseudopotential Models](https://arxiv.org/abs/2512.12934)
*[ArXiv] Fluid Dynamics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Lattice-Boltzmann, Multiphase-Flow, Numerical-Methods, Open-Boundaries

Addresses lattice Boltzmann methods with open boundaries for multiphase flows. Relevant to computational techniques for simulating complex fluid-plasma interfaces in propulsion systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2512.12934v2 Announce Type: replace Abstract: The pseudopotential lattice Boltzmann method (LBM) is a prominent approach for simulating multiphase flows, valued for its physical intuitiveness and computational tractability. However, existing immiscible pseudopotential methods for modeling dynamic multi-component immiscible fluid systems involving open boundaries face persistent challenges, notably the influence of spurious currents on interface formation and breakup, as well as the effects…

</div>
</details>

---

## [UniManip: General-Purpose Zero-Shot Robotic Manipulation with Agentic Operational Graph](https://arxiv.org/abs/2602.13086)
*[ArXiv] Robotics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Robotics, VLA

Presents agentic operational graphs for hierarchical task planning bridging semantics and control. Relevant to structured automation and agent-based reasoning in complex physical systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13086v1 Announce Type: new Abstract: Achieving general-purpose robotic manipulation requires robots to seamlessly bridge high-level semantic intent with low-level physical interaction in unstructured environments. However, existing approaches falter in zero-shot generalization: end-to-end Vision-Language-Action (VLA) models often lack the precision required for long-horizon tasks, while traditional hierarchical planners suffer from semantic rigidity when facing open-world variations. …

</div>
</details>

---

## [AstRL: Analog and Mixed-Signal Circuit Synthesis with Deep Reinforcement Learning](https://arxiv.org/abs/2602.12402)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.67**  
Published: 2026-02-16T05:00:00+00:00
Tags: Reinforcement-Learning, Circuit-Design, Optimization, Hardware-Synthesis

RL-driven design synthesis for constrained optimization in non-differentiable spaces; architecture generalizable to spacecraft power system design and thruster control circuits.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12402v1 Announce Type: new Abstract: Analog and mixed-signal (AMS) integrated circuits (ICs) lie at the core of modern computing and communications systems. However, despite the continued rise in design complexity, advances in AMS automation remain limited. This reflects the central challenge in developing a generalized optimization method applicable across diverse circuit design spaces, many of which are distinct, constrained, and non-differentiable. To address this, our work casts c…

</div>
</details>

---

## [Odd Radio Circles Modeled by Shock-Bubble Interactions](https://arxiv.org/abs/2602.12479)
*[ArXiv] Computational Physics*  
Score: **0.66**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Shock Dynamics, Computational Physics, Instabilities

3D MHD simulations of shock-plasma interactions with Richtmyer-Meshkov instability; demonstrates advanced MHD computational techniques applicable to hypersonic/plasma phenomena.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12479v1 Announce Type: cross Abstract: The physical nature and origins of the newly discovered class of Odd Radio Circles (ORCs) remain unclear. We investigate a model whereby ORCs are synchrotron-emitting vortex rings formed by the Richtmyer-Meshkov instability (RMI) when a shock interacts with a low-density fossil radio lobe in the intergalactic medium using 3D magnetohydrodynamic simulations. These rings initially exhibit oscillatory behavior that damps over time. We implement a ne…

</div>
</details>

---

## [WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2602.04634)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.66**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, MARL, Information-Seeking

Explores multi-agent width scaling for broad problem-solving, resonating with agentic R&D orchestration where parallelized teams of agents explore hypothesis spaces.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.04634v2 Announce Type: replace-cross Abstract: Recent advancements in Large Language Models (LLMs) have largely focused on depth scaling, where a single agent solves long-horizon problems with multi-turn reasoning and tool use. However, as tasks grow broader, the key bottleneck shifts from individual competence to organizational capability. In this work, we explore a complementary dimension of width scaling with multi-agent systems to address broad information seeking. Existing multi-…

</div>
</details>

---

## [Quantum-inspired space-time PDE solver and dynamic mode decomposition](https://arxiv.org/abs/2510.21767)
*[ArXiv] Computational Physics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Computational Physics, PDE Solvers

Novel approach to overcoming curse of dimensionality in PDE solving; relevant to efficient computational methods for multidimensional plasma and flow simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2510.21767v2 Announce Type: replace Abstract: The curse of dimensionality is ubiquitous in both numerical and data-driven methods. This is particularly severe for space-time methods, which treat the combined space-time domain simultaneously. We investigate the effectiveness of a quantum-inspired approach in alleviating this curse, both for solving PDEs and making data-driven predictions. We achieve this goal by treating both spatial and temporal dimensions within a single matrix product st…

</div>
</details>

---

## [Safe Reinforcement Learning via Recovery-based Shielding with Gaussian Process Dynamics Models](https://arxiv.org/abs/2602.12444)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: Safe-RL, Gaussian-Processes, Control-Systems, Aerospace

Gaussian process dynamics models with safety guarantees; applicable to spacecraft propulsion control and safety-critical RL policies in non-linear systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12444v1 Announce Type: new Abstract: Reinforcement learning (RL) is a powerful framework for optimal decision-making and control but often lacks provable guarantees for safety-critical applications. In this paper, we introduce a novel recovery-based shielding framework that enables safe RL with a provable safety lower bound for unknown and non-linear continuous dynamical systems. The proposed approach integrates a backup policy (shield) with the RL agent, leveraging Gaussian process (…

</div>
</details>

---

## [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, LLM, Architecture

Surveys composable skill-based agent architectures—foundational for building modular agentic pipelines that dynamically extend capabilities without retraining.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12430v1 Announce Type: new Abstract: The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, p…

</div>
</details>

---

## [Gradient-Enhanced Partitioned Gaussian Processes for Real-Time Quadrotor Dynamics Modeling](https://arxiv.org/abs/2602.12487)
*[ArXiv] Robotics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: Surrogates, Gaussian-Process, Real-Time, Dynamics-Modeling

Demonstrates real-time Gaussian process surrogate modeling with aerodynamic effects and uncertainty quantification. Applicable to rapid surrogate-based design for spacecraft and thruster control systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12487v1 Announce Type: new Abstract: We present a quadrotor dynamics Gaussian Process (GP) with gradient information that achieves real-time inference via state-space partitioning and approximation, and that includes aerodynamic effects using data from mid-fidelity potential flow simulations. While traditional GP-based approaches provide reliable Bayesian predictions with uncertainty quantification, they are computationally expensive and thus unsuitable for real-time simulations. To a…

</div>
</details>

---

## [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/abs/2602.13193)
*[ArXiv] Robotics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: VLA, Robotics, Control

Addresses hierarchical control via VLM-informed policies with semantic reasoning. Marginal relevance to control architecture design for complex systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13193v1 Announce Type: new Abstract: Pretrained vision-language models (VLMs) can make semantic and visual inferences across diverse settings, providing valuable common-sense priors for robotic control. However, effectively grounding this knowledge in robot behaviors remains an open challenge. Prior methods often employ a hierarchical approach where VLMs reason over high-level commands to be executed by separate low-level policies, e.g., vision-language-action models (VLAs). The inter…

</div>
</details>

---

## [An Autonomous, End-to-End, Convex-Based Framework for Close-Range Rendezvous Trajectory Design and Guidance with Hardware Testbed Validation](https://arxiv.org/abs/2602.12421)
*[ArXiv] Robotics*  
Score: **0.64**  
Published: 2026-02-16T05:00:00+00:00
Tags: Trajectory-Optimization, Spacecraft-Control, Convex-Optimization, Autonomous-Systems

Presents autonomous trajectory optimization for spacecraft rendezvous with real-time computation via convex methods. Relevant to guidance and control for electric propulsion spacecraft.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12421v1 Announce Type: new Abstract: Autonomous satellite servicing missions must execute close-range rendezvous under stringent safety and operational constraints while remaining computationally tractable for onboard use and robust to uncertainty in sensing, actuation, and dynamics. This paper presents CORTEX (Convex Optimization for Rendezvous Trajectory Execution), an autonomous, perception-enabled, real-time trajectory design and guidance framework for close-range rendezvous. CORT…

</div>
</details>

---

## [SafeFlowMPC: Predictive and Safe Trajectory Planning for Robot Manipulators with Learning-based Policies](https://arxiv.org/abs/2602.12794)
*[ArXiv] Robotics*  
Score: **0.64**  
Published: 2026-02-16T05:00:00+00:00
Tags: Control, Robotics, Learning

Combines learning-based trajectory policies with model predictive control for safety. Relevant to integration of learned models with classical optimization—a pattern applicable to propulsion simulation.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12794v1 Announce Type: new Abstract: The emerging integration of robots into everyday life brings several major challenges. Compared to classical industrial applications, more flexibility is needed in combination with real-time reactivity. Learning-based methods can train powerful policies based on demonstrated trajectories, such that the robot generalizes a task to similar situations. However, these black-box models lack interpretability and rigorous safety guarantees. Optimization-b…

</div>
</details>

---

## [RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models](https://arxiv.org/abs/2602.12628)
*[ArXiv] Robotics*  
Score: **0.63**  
Published: 2026-02-16T05:00:00+00:00
Tags: RL, Sim-Real, VLA

Demonstrates closed-loop RL-based sim-to-real co-training. Methodologically relevant to iterative training pipelines in simulation-based R&D.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12628v1 Announce Type: new Abstract: Simulation offers a scalable and low-cost way to enrich vision-language-action (VLA) training, reducing reliance on expensive real-robot demonstrations. However, most sim-real co-training methods rely on supervised fine-tuning (SFT), which treats simulation as a static source of demonstrations and does not exploit large-scale closed-loop interaction. Consequently, real-world gains and generalization are often limited. In this paper, we propose an \…

</div>
</details>

---

## [Resonant Excitation of Surface Plasmon for Wakefield Acceleration by Beating GW Lasers on Smooth Cylindrical Surface](https://arxiv.org/abs/2602.12789)
*[ArXiv] Plasma Physics*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Acceleration, Simulation

Laser-plasma acceleration mechanisms with 3D PIC simulations; tangential to electric propulsion concepts and plasma-field interactions.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12789v1 Announce Type: new Abstract: We present a theoretical and numerical study of resonant surface-plasmon (SP) excitation driven by the beating of two co-propagating laser pulses on a smooth cylindrical plasma-vacuum interface. Analytical expressions for the SP dispersion relation, field amplitude, geometric coupling factor, and resonance conditions are derived and validated by fully three-dimensional particle-in-cell simulations. We reveal that curvature-induced geometric effects…

</div>
</details>

---

## [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/abs/2602.12662)
*[ArXiv] Artificial Intelligence*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, LLM, Decision-Making, Reasoning

Proposes adaptive cognitive strategies for LLM agents in multi-turn decision-making; marginally relevant to agentic R&D pipelines through improved autonomous reasoning efficiency.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12662v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and othe…

</div>
</details>

---

## [High-dimensional Level Set Estimation with Trust Regions and Double Acquisition Functions](https://arxiv.org/abs/2602.12391)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: Active-Learning, Bayesian-Optimization, Computational-Efficiency

Active learning in high-dimensional design spaces; relevant to parameter exploration in MHD thruster optimization with expensive simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12391v1 Announce Type: new Abstract: Level set estimation (LSE) classifies whether an unknown function's value exceeds a specified threshold for given inputs, a fundamental problem in many real-world applications. In active learning settings with limited initial data, we aim to iteratively acquire informative points to construct an accurate classifier for this task. In high-dimensional spaces, this becomes challenging where the search volume grows exponentially with increasing dimensi…

</div>
</details>

---

## [Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning](https://arxiv.org/abs/2602.12633)
*[ArXiv] Robotics*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: Physics, Simulation, 3D

Addresses physics-consistent scene reconstruction for simulation. Relevant to ensuring physical validity in computational models—a concern shared with plasma simulation.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12633v1 Announce Type: new Abstract: Reconstructing physically valid 3D scenes from single-view observations is a prerequisite for bridging the gap between visual perception and robotic control. However, in scenarios requiring precise contact reasoning, such as robotic manipulation in highly cluttered environments, geometric fidelity alone is insufficient. Standard perception pipelines often neglect physical constraints, resulting in invalid states, e.g., floating objects or severe in…

</div>
</details>

---

## [Role of the radial electric field in the confinement of energetic ions in the Wendelstein 7-X stellarator](https://arxiv.org/abs/2602.12969)
*[ArXiv] Plasma Physics*  
Score: **0.61**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Confinement, Magnetic Fields

Electric field effects on ion confinement in fusion devices; relevant to understanding plasma confinement physics and control.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12969v1 Announce Type: new Abstract: Good fast-ion confinement is an essential requirement for a fusion reactor. The magnetic configuration of the Wendelstein 7-X (W7-X) stellarator is partially optimized in this regard in a reactor-relevant scenario: it is expected to show improved fast-ion confinement when $\beta$ is high and the effect of the radial electric field is negligible. The experimental validation of this optimization is difficult since, with the available power, achieving…

</div>
</details>

---
