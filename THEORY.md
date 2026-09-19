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

The algebraic coefficient extraction is fixed once an explicit typed pullback from the 36D QHTRI carrier to the three-flavour carrier is supplied.

Let

```text
H_Q in Herm(36)
```

and let `W: C^3 -> C^36` be an isometric embedding satisfying

```text
W^dagger W = I_3.
```

Define

```text
Pi_W(H_Q) = W^dagger H_Q W.
```

The result is Hermitian and transforms covariantly under a flavour basis rotation `W -> W U`:

```text
Pi_(W U)(H_Q) = U^dagger Pi_W(H_Q) U.
```

Using Gell-Mann normalization `Tr(lambda_a lambda_b)=2 delta_ab`,

```text
Pi_W(H_Q) = v0 I_3 + sum_a xi_a lambda_a,
v0 = Tr(Pi_W)/3,
xi_a = Tr(lambda_a Pi_W)/2.
```

Thus the old placeholder `xi_a = F_a(...)` is no longer an algebraic OPEN. The remaining cross-domain OPEN is the physical/provenance derivation of `Pi_{36->nu}`, represented by `W` here or by a more general typed covariant pullback. It must not be fitted to the final target observable.

For the model Euler-Berry closure on a fixed winding branch,

```text
Gamma_EBI/(2 pi) = D_Lambda + epsilon_nu + m,
```

differentiation gives

```text
dGamma_EBI/dx - 2 pi dD_Lambda/dx = 2 pi d epsilon_nu/dx.
```

For `epsilon_nu^{ij}=Delta m_ij^2 x/(4 pi E)` at fixed energy, this becomes

```text
dGamma_EBI/dx - 2 pi dD_Lambda/dx = Delta m_ij^2/(2E),
```

which is the standard mass-sector phase-rate scale. In this repository it is a consistency gate inside the model, not evidence that physical QHTRI-neutrino coupling has been observed.

See `docs/T36_TO_U3_PULLBACK.md`.

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
