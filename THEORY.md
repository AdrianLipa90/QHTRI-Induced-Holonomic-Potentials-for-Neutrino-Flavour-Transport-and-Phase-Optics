# Theory Core v0.1

## 1. Baseline flavour transport

Use natural units unless a module explicitly declares otherwise. Let

```text
|nu(x)> in C^3
```

be the flavour state. The baseline evolution is

```text
i d|nu>/dx = H_base(x) |nu>,
H_base = H_vac + V_MSW.
```

A convenient vacuum form is

```text
H_vac = U diag(m_1^2, m_2^2, m_3^2) U^dagger / (2E),
```

up to an irrelevant multiple of the identity. For ordinary matter,

```text
V_MSW = diag(V_CC, 0, 0)
```

in the flavour basis for neutrinos, with the appropriate sign change for antineutrinos.

This baseline is a control, not a result of QHTRI.

## 2. QHTRI state and closed-loop holonomy

For a 36-mode phase state, define

```text
|psi_Q> = (1/sqrt(36)) [exp(i phi_1), ..., exp(i phi_36)]^T
```

for equal amplitudes, or its normalized amplitude-weighted generalisation.

For a discrete closed path of normalized states `psi_0,...,psi_{N-1}`, define the Pancharatnam/Berry holonomy

```text
Gamma_Q = arg prod_k <psi_k | psi_(k+1 mod N)>.
```

The closed product is invariant under independent global rephasing

```text
psi_k -> exp(i alpha_k) psi_k.
```

This provides a gauge-clean observable on the computational QHTRI path.

## 3. Working Euler-Berry closure

The project tracks the model relation

```text
Gamma_Q/(2 pi) = D + epsilon_nu + m + delta_close,
```

where `m` is an integer winding sector and `delta_close` is the wrapped residual.

This equation is **DERIVED_IN_MODEL / HYPOTHESIS-BRIDGE**. Its use in software does not establish that `D`, `epsilon_nu`, or `Gamma_Q` are physically coupled in nature.

## 4. Flavour-space holonomic potential

The minimal effective extension is

```text
H_eff = H_base + V_Q,
V_Q = v0 I_3 + sum_(a=1)^8 xi_a lambda_a,
```

where `lambda_a` are Gell-Mann generators and real `xi_a` ensure Hermiticity.

The scalar part `v0 I_3` contributes only a common phase. Flavour-selective transport requires a nontrivial traceless component or a noncommuting path-dependent connection.

For a path-dependent matrix potential, the propagator is

```text
U(C) = P exp[-i integral_C H_eff(x) dx].
```

If

```text
[V_Q(x1), V_Q(x2)] != 0,
```

path ordering becomes physically relevant within the model and the transport can be non-Abelian in flavour space.

## 5. QHTRI-to-potential bridge

The research question is to derive, rather than assume, a map

```text
Q(x,t) -> xi_a(x,t),
```

where `Q` contains measurable oscillator observables such as amplitudes, phases, cross-correlations, spectra, and closed-path holonomy.

A generic placeholder is

```text
xi_a = F_a(C_ij, S_ij(omega), Delta phi_ij, Gamma_Q, ...).
```

The functions `F_a` are not fixed by standard physics. They are the central object to constrain or falsify experimentally.

## 6. Phase optics

For an effective propagation eigenmode `a`, a thin-lens phase target is

```text
Phi_a(r) = Phi_a0 - k_a r^2/(2 f_a).
```

Its transverse curvature is

```text
d^2 Phi_a/dr^2 = -k_a/f_a.
```

The project therefore distinguishes:

```text
phase steering:   grad_perp Phi != 0
phase focusing:   Hessian_perp Phi != 0
```

A flavour-selective optical element requires mode-dependent phase curvature. Demonstrating a programmed `Gamma_Q(r)` in software is not equivalent to demonstrating a physical neutrino lens.

## 7. Effective geometry vs spacetime geometry

An effective matrix-valued transport geometry may be written schematically as

```text
G_eff = g_mu_nu tensor I_3 + Delta G_mu_nu^a lambda_a.
```

This notation is useful for organising transport, but it must not be interpreted automatically as a modification of the Einstein metric. The repository keeps two hypotheses separate:

```text
HνQ: QHTRI -> effective neutrino/flavour Hamiltonian
Hg:  QHTRI -> physical spacetime metric perturbation
```

`HνQ` does not imply `Hg`.

## 8. Falsification invariants

Every implementation must preserve the following controls:

1. `V_Q=0` recovers the baseline Hamiltonian.
2. `V_Q=v0 I` leaves flavour probabilities unchanged for a fixed baseline evolution, apart from numerical tolerance.
3. `V_Q` must be Hermitian before unitary propagation is claimed.
4. Closed holonomy must be invariant under local global rephasing of each sampled state.
5. A focusing claim requires spatially resolved output and a pre-registered null/control condition.
6. Physical promotion requires hardware data; CPU/GPU execution is not evidence of physical neutrino coupling.
