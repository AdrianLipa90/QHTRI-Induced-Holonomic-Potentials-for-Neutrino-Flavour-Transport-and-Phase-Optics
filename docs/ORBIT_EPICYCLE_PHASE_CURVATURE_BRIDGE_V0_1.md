# Orbit / Epicycle -> Phase-Curvature Bridge v0.1

Status: `EXACT_RADIAL_SCALAR_IDENTITY / PHASE_OPTICS_BRIDGE / SPACETIME_PROMOTION_OPEN`

This bridge expresses the transverse gradient and Hessian of a spherical scalar potential in terms of circular-orbit and epicyclic observables. It is an algebraic bridge inside a shared scalar-potential model. It does not establish that the scalar is a spacetime metric perturbation.

## 1. Radial scalar from orbital observables

For a differentiable spherical scalar (Phi(r)),

[
Omega^2(r)=rac{Phi'(r)}{r}.
]

Hence

[
oxed{Phi'(r)=rOmega^2(r).}
]

The epicyclic frequency obeys

[
oxed{
kappa_{m epi}^2
=
Phi''+rac{3}{r}Phi'
=
4Omega^2+rrac{dOmega^2}{dr}.
}
]

Therefore

[
oxed{Phi''=kappa_{m epi}^2-3Omega^2.}
]

In three dimensions, the radial Hessian eigenvalues are

[
oxed{
lambda_r=kappa_{m epi}^2-3Omega^2,
qquad
lambda_{t1}=lambda_{t2}=Omega^2.
}
]

## 2. Transverse phase gradient

Let a ray coordinate have impact parameter (b) and line coordinate (z),

[
r=sqrt{b^2+z^2}.
]

Then

[
rac{partialPhi}{partial b}
=
Phi'(r)rac{b}{r},
]

so

[
oxed{
rac{partialPhi}{partial b}
=
bOmega^2(r).
}
]

This gives the scalar steering kernel directly from the orbital field.

## 3. Transverse curvature

Differentiation gives

[
rac{partial^2Phi}{partial b^2}
=
rac{b^2}{r^2}Phi''
+
left(1-rac{b^2}{r^2}ight)rac{Phi'}{r}.
]

Using the orbital identities,

[
oxed{
rac{partial^2Phi}{partial b^2}
=
rac{b^2}{r^2}kappa_{m epi}^2
+
left(1-rac{4b^2}{r^2}ight)Omega^2.
}
]

Thus ((Omega,kappa_{m epi})) determine the local transverse scalar curvature under the declared spherical model.

## 4. Control families

For (Omega^2=A r^{-q}),

[
kappa_{m epi}^2=(4-q)Omega^2.
]

Therefore:

- Kepler (q=3): Hessian eigenvalues ((-2,1,1)Omega^2);
- flat rotation (q=2): ((-1,1,1)Omega^2);
- solid body (q=0): ((1,1,1)Omega^2).

These are scalar-potential curvature signatures, not by themselves gravitational-lensing claims.

## 5. Information-potential interface

If the independently admitted RFC bridge supplies

[
U_I=c_IXi_I
]

and the phase-optics route supplies

[
Phi_I[C]=-int_Cchi_phi U_I,ds,
]

then the existing information-gradient/Hessian machinery can consume the same scalar derivatives. The algebraic equality of derivatives does not calibrate (c_I) or establish a physical carrier.

## 6. Metric firewall

The following implication is NOT admitted by this bridge:

[
(Omega,kappa_{m epi})
Rightarrow
g_{mu
u}.
]

A physical gravitational-lensing or spacetime-curvature claim still requires the separate (H_g) bridge and its source/normalization evidence.

## 7. Cross-repository links

- IDT 02JQ:
  https://github.com/AdrianLipa90/Informational-Dynamics-of-Time/blob/candidate/idt-eb-bec-orbital-acoustic-v0.1/formalism/02JQ_radial_condensate_profile_classification.md
- GREMLIN radial identifiability:
  https://github.com/AdrianLipa90/GREMLIN/blob/integrate/relational-phase-observation-v0.1/spec/GREMLIN_RADIAL_MEDIUM_IDENTIFIABILITY_V0_1.md
- Resonant Chemistry holonomy:
  https://github.com/AdrianLipa90/Resonant-Chemistry/blob/integrate/relational-phase-observation-v0.1/THEORY/15_RELATIONAL_HOLONOMY_SPECTROSCOPY_BRIDGE_V0_1.md
- OES holonomy response:
  https://github.com/AdrianLipa90/Orbital-Eclipse-Spectroscopy/blob/integrate/relational-phase-observation-v0.1/formalism/OES_H1_HOLONOMY_RESPONSE_IDENTIFIABILITY_V0_1.md
- FPDG:
  https://github.com/AdrianLipa90/Fundamental-Physics-Dependency-Graph
