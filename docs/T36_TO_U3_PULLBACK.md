# T36/QHTRI to U(3) Flavour Pullback

## Status

MATHEMATICAL INTERFACE: DERIVED / IMPLEMENTED

PHYSICAL IDENTIFICATION OF THE EMBEDDING: OPEN / PHYSICAL_HYPOTHESIS

This note closes the algebraic part of the previously open `F_a` question without inventing a direct identification of 36 PhaseNav dimensions with three neutrino flavours.

## Source chain

The derivation uses four existing project statements:

1. QHTRI carries a finite Hermitian 36-mode operator with complex magnetic/Pancharatnam-Bargmann edge phases and an exact finite quantum lift.
2. TIR owns an explicit three-flavour carrier `C^3` with mixing algebra `su(3)_F`, hence eight independent traceless Hermitian mixing directions.
3. NEUTRINOTIME -> T36 Integration V1 explicitly requires a typed map `Pi_{36->nu}: T^36 -> u(3)`, with provenance, Hermiticity, gauge rule, sensitivity and zero-map ablation.
4. The Euler-Berry closure relates the accumulated EBI holonomy to `D_Lambda + epsilon_nu + integer winding`.

No canonical source was found that identifies the 36 T36 coordinates directly with the three flavours or that proves a `36 = 24 + 12` flavour decomposition. This repository therefore does not invent one.

## Typed pullback

Let the QHTRI operator be

    H_Q in Herm(36).

Let

    W: C^3 -> C^36

be an isometric embedding with

    W^dagger W = I_3.

Define

    Pi_W(H_Q) = W^dagger H_Q W.

Because `H_Q` is Hermitian, `Pi_W(H_Q)` is Hermitian and therefore lies in `u(3)` under the Hermitian-generator convention.

Under a flavour-basis rotation `W -> W U`, with `U in U(3)`,

    Pi_{WU}(H_Q) = U^dagger Pi_W(H_Q) U.

Thus the pullback is basis covariant.

## Canonical coefficient extraction

Using Gell-Mann generators normalized by

    Tr(lambda_a lambda_b) = 2 delta_ab,

write

    Pi_W(H_Q) = v0 I_3 + sum_{a=1}^8 xi_a lambda_a.

Then no regression or arbitrary coefficient fit is needed:

    v0 = Tr(Pi_W)/3,

    xi_a = (1/2) Tr(lambda_a Pi_W).

Therefore the old placeholder

    xi_a = F_a(...)

is algebraically closed once the typed physical pullback `Pi_{36->nu}` is supplied.

The actual remaining OPEN is the provenance/physical derivation of `W` (or a more general covariant `Pi`), not the SU(3) coefficient functional.

## Euler-Berry differential consistency

For a fixed winding branch,

    Gamma_EBI/(2 pi) = D_Lambda + epsilon_nu + m.

Differentiating along path coordinate `x` gives

    dGamma_EBI/dx - 2 pi dD_Lambda/dx
      = 2 pi d epsilon_nu/dx.

For a single fixed-energy oscillation channel,

    epsilon_nu^{ij} = Delta m_ij^2 x / (4 pi E),

hence

    dGamma_EBI/dx - 2 pi dD_Lambda/dx
      = Delta m_ij^2 / (2E).

The right-hand side is exactly the standard mass-sector phase-rate scale in the neutrino Hamiltonian. In this repository this is used as a model-consistency gate, not as experimental proof of QHTRI-neutrino coupling.

## Hard gates for W / Pi

Any physical candidate embedding must be frozen before target-data analysis and carry:

- source/provenance identifier;
- normalization/unit contract;
- `W^dagger W = I_3` gate, or the corresponding contract for a more general pullback;
- Hermiticity gate;
- flavour-basis covariance test;
- sensitivity analysis under perturbations of W;
- zero-coupling / zero-map ablation;
- randomized-map control;
- no fitting to the final neutrino observable used to claim the coupling.

## Consequence

The chain is now

    H_QHTRI(36D)
      -> Pi_{36->nu}
      -> u(3)
      -> [v0, xi_1,...,xi_8]
      -> H_geom
      -> path-ordered flavour propagation.

Only `Pi_{36->nu}` remains a physical/cross-domain identification problem.
