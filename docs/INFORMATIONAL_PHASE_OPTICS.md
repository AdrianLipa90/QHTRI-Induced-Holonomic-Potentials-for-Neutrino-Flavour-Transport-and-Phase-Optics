# Informational Phase Optics

Status: DERIVED_MODEL_INTERFACE / SUBSTRATE-INVARIANT_FUNCTIONAL / CARRIER_COUPLING_TYPED_SEPARATELY

Date: 2026-09-19

## 1. Parent potential

RFC RF-L3 supplies the admitted information-scalar potential

    Xi_I = J_pi / A_rel,
    U_I = (alpha_I / kappa_E) Xi_I,

where J_pi is the natural-log relative information D_KL(p || pi). RF-L4A supplies the local Shannon-Fisher normalization near the stationary reference.

Therefore the potential is a functional of the typed relational state, not of a named computational substrate.

## 2. Observation/update theorem

Let an admitted observation or update send the relational probability state

    p -> p_y

and optionally the relational area

    A_rel -> A_rel,y.

Then the potential shift is exactly

    Delta U_I(y)
      = (alpha_I / kappa_E)
        [ D_KL(p_y || pi)/A_rel,y - D_KL(p || pi)/A_rel ].

For fixed relational area this reduces to

    Delta U_I(y)
      = alpha_I / (kappa_E A_rel)
        [ D_KL(p_y || pi) - D_KL(p || pi) ].

This is an algebraic consequence of the RF-L3 potential definition. No substrate label occurs in the expression.

Important firewall: an update of p does not guarantee Delta U_I != 0. The update must change Xi_I. Equal-information updates can leave the scalar potential unchanged.

## 3. Substrate invariance

For any two realizations R1 and R2 that instantiate the same typed tuple

    (p, pi, A_rel, alpha_I, kappa_E),

the reconstructed potential is identical:

    U_I[R1] = U_I[R2].

This is functional substrate invariance. It is a theorem about the admitted informational potential, not a claim that every physical observable or every carrier coupling is substrate independent.

## 4. Potential to phase

A carrier-specific phase interface must still declare the factor converting the potential coordinate to accumulated dimensionless phase. Denote the integrated factor by chi_phi. Then

    Phi_I = - chi_phi U_I

for a constant phase-screen segment, or schematically

    Phi_I[C] = - integral_C chi_phi(s) U_I(s) ds.

The project does not infer chi_phi from RF-L3. It is part of the carrier/representation binding.

Once chi_phi is fixed, an observation-induced potential shift produces

    Delta Phi_I(y)
      = - integral_C chi_phi(s) Delta U_I(y,s) ds.

## 5. Informational steering and focusing

For constant alpha_I, kappa_E and chi_phi along the transverse differentiation:

    grad_perp Phi_I
      = - integral chi_phi alpha_I/kappa_E grad_perp Xi_I ds,

    Hess_perp Phi_I
      = - integral chi_phi alpha_I/kappa_E Hess_perp Xi_I ds.

Therefore:

    uniform Delta Xi_I      -> common phase shift only
    grad Delta Xi_I != 0    -> steering
    Hess Delta Xi_I != 0    -> focusing/defocusing

The same statement applies to observation-induced changes Delta Xi_I.

## 6. Relation to flavour optics

A scalar informational potential multiplied by I_3 can modify a spatial wavefront while leaving internal flavour probabilities unchanged. This is consistent with the existing M1 null:

    scalar V_I(x) I_3
      -> spatial phase may vary with x
      -> no flavour-selective conversion from the scalar term alone.

Flavour-selective optics requires a mode-dependent or traceless Hermitian component, for example through the typed pullback or oriented-edge route already implemented in this repository.

## 7. Simulation status

A simulation that realizes the admitted relational state and evaluates the exact functional above is a realization of the informational-potential dynamics at model level. It can establish:

- the exact observation/update -> potential response;
- phase-screen response after a declared chi_phi;
- steering/focusing from spatial gradients and Hessians;
- invariance under changing implementation while preserving the typed relational state.

It does not by itself establish an otherwise-unbound physical neutrino/QHTRI carrier coupling. That is a separate map.

## 8. Source lineage

Primary parent surfaces:

- Relational-Field-Closure/closure/lambda0/RF_L3_INFORMATION_SCALAR_POTENTIAL_RECONSTRUCTION.md
- Relational-Field-Closure/closure/lambda0/RF_L4_INFORMATION_CURVATURE_CANONICAL_PULLBACK.md
- Relational-Field-Closure/closure/lambda0/RF_L4A_SHANNON_FISHER_LOCAL_NORMALIZATION.md
- Relational-Field-Closure/closure/lambda0/RF_L5_SHANNON_ONSAGER_TEMPORAL_WAVE_KLEIN_GORDON_BRIDGE.md

RF-L3 already preserves the oriented holonomy coordinate tau_R alongside Xi_I. The present interface composes that information-potential lineage with phase optics without identifying the scalar RFC potential with a neutrino Hamiltonian before an explicit carrier coupling is declared.

## 11. Downstream mechanics cross-reference

The potential/phase functional is extended into momentum, lens-Jacobian, standard gravitational-lensing cross-checks and the GREMLIN orbital/EB frontier in:

`docs/PHASE_MECHANICS_GREMLIN_ORBITAL_EB_BRIDGE.md`

That document preserves the firewall between derived phase mechanics and the OPEN physical source binding of an EB-condensate orbital carrier.
