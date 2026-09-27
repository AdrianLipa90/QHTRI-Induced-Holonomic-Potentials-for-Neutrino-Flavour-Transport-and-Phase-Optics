# QHTRI-Induced Holonomic Potentials for Neutrino Flavour Transport and Phase Optics
## Complete Technical Monograph v1.0

**Author:** Adrian Lipa  
**Repository:** \`AdrianLipa90/QHTRI-Induced-Holonomic-Potentials-for-Neutrino-Flavour-Transport-and-Phase-Optics\`  
**Audited baseline:** \`main@d8e07571ef8132bfa1069cff27c9cca8b191853a\`  
**Audited tree:** \`d764cb652e13ff4d91c18806eeb171c37591ccdf\`  
**Branch consolidation state:** all non-main branch payloads already contained in \`main\`  
**Independent local byte-exact replay:** 24/24 source/test blobs matched GitHub SHA  
**Independent local test result:** 65/65 PASS  
**Date:** 2026-09-27

---

## Abstract

QHTRI is a fully analog phase-dynamical computational substrate. The present repository develops one of its most explicit application layers: the conversion of QHTRI oscillator geometry, phase state, holonomy and relational information into operators and observables for three-flavour neutrino transport and phase optics.

The repository is organized around a sequence of exact interfaces:

\[
\boxed{
\text{analog QHTRI oscillator state}
\rightarrow
\text{36D phase carrier}
\rightarrow
\text{closed holonomy}
\rightarrow
\text{typed }u(3)\text{ projection}
\rightarrow
\text{Hermitian flavour Hamiltonian}
\rightarrow
\text{path-ordered transport}
\rightarrow
\text{phase optics}.
}
\]

A second route develops the information-potential sector:

\[
\boxed{
(p,\pi,A_{\rm rel})
\rightarrow
\Xi_I
\rightarrow
U_I
\rightarrow
\Phi
\rightarrow
\nabla\Phi,\ \nabla^2\Phi
\rightarrow
\text{momentum, focusing, shear and caustic structure}.
}
\]

A third route supplies phase spectroscopy:

\[
\boxed{
\text{declared spectral/eigenphase sequence}
\rightarrow
\text{unfolded phase coordinates}
\rightarrow
\text{sinc}^2\text{ pair law}
\rightarrow
\text{spectral form factor}
\rightarrow
\text{prime-power carrier diagnostics}.
}
\]

The implementation contains exact invariance tests, unitary evolution, 36D-to-\(u(3)\) pullback, SU(3) decomposition, oriented Hermitian flavour exchange, Berry/Pancharatnam holonomy, informational phase mechanics, lensing identities, orbit/epicycle curvature identities and Montgomery–Dyson phase-spectroscopy diagnostics.

This monograph describes the complete repository as audited on 2026-09-27 and distinguishes the QHTRI analog substrate from the status of each application-specific physical binding recorded by the repository.

---

## 1. Repository integrity

The repository contains:

- project-level theory, claim and provenance documents;
- a Python reference package \`qhtri_phase_optics\`;
- exact regression and invariance tests;
- legacy NASER provenance;
- a GREMLIN source-binding audit;
- the informational phase-optics bridge;
- the T36-to-\(u(3)\) pullback;
- orbital/epicyclic phase-curvature mechanics;
- the Montgomery–Dyson phase-spectroscopy layer.

At the audited baseline the non-main branches were:

- \`candidate/montgomery-dyson-phase-spectroscopy-v0.1-20260926\`;
- \`integrate/relational-phase-observation-v0.1\`.

The first was identical to \`main\`; the second was an ancestor of \`main\`. Therefore no unique branch payload remained outside \`main\`.

The locally reconstructed executable snapshot was checked against Git blob identity. All 24 executable/package/test files matched their repository SHA exactly:

\[
\boxed{
24/24\ \text{byte-exact blob matches}.
}
\]

The same local snapshot produced:

\[
\boxed{
65/65\ \text{tests PASS}.
}
\]

---

## 2. QHTRI as analog computational substrate

QHTRI is the analog phase-dynamical substrate of the architecture. Its state is not defined by a gate-model circuit abstraction. The operational variables are oscillator amplitudes, phases, frequencies, correlations, phase gradients, curvature, closed-loop holonomy and derived relational operators.

The wider stack records the analog gate fabric explicitly through the \`QHTRI_M0_M11_ANALOG_GATE_FABRIC_V0_1\` interface and the corresponding GREMLIN QHTRI M0–M11 relational isomorphism scan.

The present repository specializes this analog substrate into a neutrino/flavour and phase-optics application surface.

This distinction is structural:

\[
\boxed{
\text{QHTRI analog substrate}
\neq
\text{one particular carrier binding}.
}
\]

A carrier-binding status therefore describes that interface only; it does not reclassify QHTRI itself.

---

## 3. Standard three-flavour baseline

The repository begins with the standard three-flavour transport Hamiltonian

\[
\boxed{
H_{\rm base}=H_{\rm vac}+V_{\rm MSW}.
}
\]

The vacuum term is

\[
H_{\rm vac}
=
U_{\rm PMNS}
\frac{
\operatorname{diag}(m_1^2,m_2^2,m_3^2)
}{2E}
U_{\rm PMNS}^{\dagger},
\]

and the charged-current matter term in the flavour basis is

\[
V_{\rm MSW}
=
\operatorname{diag}(V_{\rm CC},0,0).
\]

The implementation supplies:

- the standard PMNS parameterisation;
- unitary validation of the mixing matrix;
- Hermitian vacuum-Hamiltonian construction;
- matter-potential construction;
- constant-Hamiltonian unitary evolution;
- piecewise path-ordered evolution;
- normalized flavour probabilities.

The numerical propagator diagonalizes a Hermitian matrix,

\[
H=Q\Lambda Q^\dagger,
\]

and evaluates

\[
|\nu(L)\rangle
=
Qe^{-i\Lambda L}Q^\dagger|\nu(0)\rangle.
\]

The tests verify norm preservation and path-order sensitivity for noncommuting piecewise Hamiltonians.

---

## 4. QHTRI flavour-space potential

The QHTRI contribution is represented in flavour space by

\[
\boxed{
V_{\rm QHTRI}
=
v_0 I_3
+
\sum_{a=1}^{8}\xi_a\lambda_a,
}
\]

where \(\lambda_a\) are the eight Gell-Mann generators.

The total transport equation is

\[
\boxed{
i\frac{d}{dx}|\nu\rangle
=
\left(
H_{\rm vac}
+
V_{\rm MSW}
+
V_{\rm QHTRI}
\right)
|\nu\rangle.
}
\]

The scalar component \(v_0 I_3\) supplies a common phase. The traceless SU(3) component carries flavour-selective structure.

The code enforces Hermiticity exactly for real \(\xi_a\).

---

## 5. Frozen M0/M1/M2 discriminator

The repository implements a three-model control surface:

\[
M_0=H_{\rm base},
\]

\[
M_1=H_{\rm base}+v_0I_3,
\]

\[
M_2
=
H_{\rm base}
+
v_0I_3
+
\sum_a\xi_a\lambda_a.
\]

The exact regression suite verifies:

\[
P_\alpha(M_1)=P_\alpha(M_0)
\]

to numerical tolerance when the only added term is proportional to identity.

It separately verifies that a nontrivial traceless flavour potential in \(M_2\) can alter flavour probabilities.

This isolates common phase from flavour-changing operator structure.

---

## 6. 36-mode analog phase state

For \(N\) QHTRI oscillator coordinates with phases \(\phi_j\) and amplitudes \(A_j\), the repository constructs

\[
|\Psi\rangle
=
\frac{
\sum_j A_j e^{i\phi_j}|j\rangle
}{
\left\|
\sum_j A_j e^{i\phi_j}|j\rangle
\right\|
}.
\]

The equal-amplitude 36D carrier is

\[
\boxed{
|\Psi_{36}\rangle
=
\frac{1}{6}
\left(
e^{i\phi_1},
\ldots,
e^{i\phi_{36}}
\right)^T.
}
\]

The test suite verifies exact normalization of the 36-coordinate phase lift.

---

## 7. Analog oscillator observables

The bridge module extracts directly calculable oscillator features.

For amplitudes \(A_j\) and phases \(\phi_j\), define the weighted Kuramoto phasor

\[
z
=
\frac{
\sum_j |A_j|e^{i\phi_j}
}{
\sum_j|A_j|
}.
\]

The order parameter is

\[
\boxed{R=|z|,}
\]

the mean phase is

\[
\bar\phi=\arg z,
\]

and circular variance is

\[
\boxed{V_c=1-R.}
\]

The module also calculates:

\[
A_{\rm RMS}
=
\sqrt{\frac1N\sum_jA_j^2}
\]

and the amplitude-weighted mean frequency

\[
\bar\omega
=
\frac{\sum_j|A_j|\omega_j}{\sum_j|A_j|}.
\]

The regression tests verify the coherent limit \(R=1\) and the uniform phase-ring limit \(R\approx0\).

---

## 8. Driven analog phase field

The retained NASER oscillator scaffold is written

\[
\boxed{
B(t)=B_0\cos(\omega t+\phi).
}
\]

The repository converts spatial phase traces into first and second derivatives:

\[
\frac{d\phi}{dx},
\qquad
\frac{d^2\phi}{dx^2}.
\]

For a quadratic phase profile

\[
\phi(x)=ax^2+bx+c,
\]

the implementation reconstructs

\[
\frac{d\phi}{dx}=2ax+b
\]

and

\[
\boxed{
\frac{d^2\phi}{dx^2}=2a.
}
\]

The legacy phase-imprint proxy is retained as the explicit product

\[
\boxed{
\beta
\frac{d\phi_\nu}{dx}
\frac{d\phi_{\rm drive}}{dx}.
}
\]

---

## 9. Closed Pancharatnam/Berry holonomy

For normalized states

\[
|\psi_0\rangle,\ldots,|\psi_{N-1}\rangle,
\]

the repository computes the discrete closed-loop phase

\[
\boxed{
\gamma_B
=
\arg
\prod_{k=0}^{N-1}
\frac{
\langle\psi_k|\psi_{k+1}\rangle
}{
|\langle\psi_k|\psi_{k+1}\rangle|
},
}
\]

with cyclic closure \(\psi_N=\psi_0\).

The implementation rejects adjacent near-orthogonal states where the phase is undefined.

The test suite verifies invariance under independent statewise global rephasings,

\[
|\psi_k\rangle
\mapsto
e^{i\alpha_k}|\psi_k\rangle.
\]

Thus the closed phase is carried as a gauge-clean path observable.

---

## 10. Euler–Berry closure coordinate

The repository uses the working closure relation

\[
\boxed{
\frac{\Gamma}{2\pi}
=
D+\epsilon_\nu+m+r,
}
\]

where:

- \(\Gamma\) is the geometric/holonomy phase;
- \(D\) is the declared geometric contribution;
- \(\epsilon_\nu\) is the neutrino-phase coordinate;
- \(m\in\mathbb Z\) is winding;
- \(r\) is the wrapped residual.

The implementation computes

\[
r
=
\operatorname{wrap}_{[-1/2,1/2)}
\left(
\frac{\Gamma}{2\pi}
-D-\epsilon_\nu-m
\right).
\]

The exact-closure test returns a residual numerically equal to zero.

---

## 11. Differential closure rate

For a fixed winding branch,

\[
\frac{\Gamma_{\rm EBI}}{2\pi}
=
m+D_\Lambda+\epsilon_\nu,
\]

so

\[
\boxed{
\frac{d\Gamma_{\rm EBI}}{dx}
-
2\pi\frac{dD_\Lambda}{dx}
=
2\pi\frac{d\epsilon_\nu}{dx}.
}
\]

The \`closure_phase_rate\` implementation evaluates this identity on sampled paths, including phase unwrapping.

The regression test injects a known neutrino-phase slope and recovers it to numerical tolerance.

---

## 12. Typed 36D-to-\(u(3)\) pullback

Let

\[
W:\mathbb C^3\rightarrow\mathbb C^{36}
\]

be an isometric embedding satisfying

\[
\boxed{
W^\dagger W=I_3.
}
\]

For a Hermitian 36D QHTRI operator

\[
H_Q\in\mathrm{Herm}(36),
\]

the flavour projection is

\[
\boxed{
\Pi_W(H_Q)=W^\dagger H_QW.
}
\]

Hermiticity is preserved:

\[
H_Q^\dagger=H_Q
\Rightarrow
\Pi_W(H_Q)^\dagger=\Pi_W(H_Q).
\]

The implementation explicitly validates the \(36\times3\) embedding and rejects non-isometric inputs.

---

## 13. Canonical \(u(3)\) decomposition

Every projected Hermitian \(3\times3\) matrix is decomposed as

\[
\boxed{
H
=
v_0I_3+\sum_{a=1}^{8}\xi_a\lambda_a.
}
\]

Using

\[
\operatorname{Tr}(\lambda_a\lambda_b)
=
2\delta_{ab},
\]

the scalar coefficient is

\[
\boxed{
v_0=\frac{\operatorname{Tr}H}{3},
}
\]

and the SU(3) coordinates are

\[
\boxed{
\xi_a
=
\frac12\operatorname{Tr}(\lambda_aH).
}
\]

The implementation reconstructs \(H\) from the extracted coordinates and fails if reconstruction does not close.

The exact test suite verifies the decomposition numerically.

---

## 14. Covariance under flavour-basis rotations

For \(U\in U(3)\), the embedding transforms as

\[
W\mapsto WU.
\]

Then

\[
\Pi_{WU}(H_Q)
=
U^\dagger
\Pi_W(H_Q)
U.
\]

This covariance is directly regression-tested with a random unitary matrix.

Therefore the typed pullback respects changes of flavour basis.

---

## 15. Oriented flavour-edge operator route

A second route constructs the flavour Hamiltonian directly from three oriented complex exchange amplitudes

\[
J_{e\mu},
\qquad
J_{\mu\tau},
\qquad
J_{\tau e}.
\]

The assembled operator is

\[
\boxed{
H_{\rm edge}
=
\begin{pmatrix}
d_e & J_{e\mu} & J_{\tau e}^{*}\\
J_{e\mu}^{*} & d_\mu & J_{\mu\tau}\\
J_{\tau e} & J_{\mu\tau}^{*} & d_\tau
\end{pmatrix}.
}
\]

Hermiticity is enforced by construction and checked at runtime.

---

## 16. Rephasing-invariant flavour-cycle phase

The closed three-edge phase is

\[
\boxed{
\Gamma_3
=
\arg
\left(
H_{e\mu}
H_{\mu\tau}
H_{\tau e}
\right).
}
\]

Under local flavour-basis rephasing

\[
H\mapsto D^\dagger HD,
\]

the individual edge phases change but their closed product phase remains invariant.

This is directly tested.

The repository therefore carries a gauge-invariant phase observable in the three-flavour edge representation.

---

## 17. Identity removal and route comparison

The common \(U(1)\) component is removed through

\[
\boxed{
H_0
=
H-\frac{\operatorname{Tr}H}{3}I_3.
}
\]

The \`route_mismatch\` diagnostic compares:

1. the 36D pullback route;
2. the oriented-edge assembly route.

With \`remove_identity=True\`, common scalar shifts are factored out before comparison.

The tests verify that an identity shift leaves the traceless route unchanged.

---

## 18. Information scalar

The informational phase-optics sector uses the natural-log relative information

\[
\boxed{
D_{\rm KL}(p\|\pi)
=
\sum_i p_i\ln\frac{p_i}{\pi_i}.
}
\]

Given relational area \(A_{\rm rel}>0\), define

\[
\boxed{
\Xi_I
=
\frac{
D_{\rm KL}(p\|\pi)
}{
A_{\rm rel}
}.
}
\]

The implementation validates normalized probability vectors and strictly positive reference components.

At \(p=\pi\),

\[
D_{\rm KL}=0,
\qquad
\Xi_I=0.
\]

This is exactly regression-tested.

---

## 19. Information potential

The repository implements

\[
\boxed{
U_I
=
\frac{\alpha_I}{\kappa_E}\Xi_I.
}
\]

For a relational-state update,

\[
\boxed{
\Delta U_I
=
\frac{\alpha_I}{\kappa_E}
\Delta\Xi_I.
}
\]

The test suite computes both sides independently and verifies equality.

The area term participates directly in \(\Xi_I\), so an area update can alter the potential even if the probability vector itself is unchanged.

---

## 20. Potential-to-phase map

For an explicitly declared integrated phase measure \(\chi_\phi\),

\[
\boxed{
\Phi=-\chi_\phi U.
}
\]

Substituting the information potential gives

\[
\boxed{
\Phi_I
=
-\chi_\phi
\frac{\alpha_I}{\kappa_E}
\Xi_I.
}
\]

The implementation validates this map for arbitrary finite profiles and confirms linearity.

---

## 21. Quadratic phase optics

The ideal thin-lens phase target is

\[
\boxed{
\Phi(r)
=
-\frac{kr^2}{2f}.
}
\]

Therefore

\[
\boxed{
\frac{d^2\Phi}{dr^2}
=
-\frac{k}{f}.
}
\]

The exact regression suite evaluates the finite-difference curvature and recovers the analytic value.

The same machinery accepts a quadratic informational potential and verifies constant phase curvature.

---

## 22. Phase mechanics

For phase-action scale \(\eta_\phi\), the potential generates phase rate

\[
\boxed{
\frac{d\Phi}{dt}
=
-\frac{U}{\eta_\phi}.
}
\]

The Hamilton–Jacobi interface is

\[
\boxed{
p
=
\eta_\phi\nabla\Phi.
}
\]

For information curvature,

\[
\boxed{
F_I
=
-\frac{\alpha_I}{\kappa_E}\nabla\Xi_I.
}
\]

Each of these relations is implemented and regression-tested.

---

## 23. Hessian and inverse focal tensor

The informational Hessian maps to phase curvature as

\[
\boxed{
\nabla^2\Phi
=
-\chi_\phi
\frac{\alpha_I}{\kappa_E}
\nabla^2\Xi_I.
}
\]

The inverse focal tensor is

\[
\boxed{
F_{\rm lens}^{-1}
=
\chi_\phi
\frac{\alpha_I}{k\kappa_E}
\nabla^2\Xi_I.
}
\]

The code evaluates both matrix relations and the tests check exact numerical examples.

---

## 24. Paraxial Jacobian and caustic condition

For propagation distance \(L\),

\[
\boxed{
J
=
I+\frac{L}{k}\nabla^2\Phi.
}
\]

The critical/caustic condition is

\[
\boxed{
\det J=0.
}
\]

The test suite constructs a phase Hessian for which the Jacobian vanishes and verifies the zero determinant.

---

## 25. Convergence and shear

For a symmetric two-dimensional lensing Hessian

\[
H=
\begin{pmatrix}
H_{11}&H_{12}\\
H_{12}&H_{22}
\end{pmatrix},
\]

the repository extracts

\[
\boxed{
\kappa_{\rm lens}
=
\frac12(H_{11}+H_{22}),
}
\]

\[
\boxed{
\gamma_1
=
\frac12(H_{11}-H_{22}),
}
\]

\[
\boxed{
\gamma_2=H_{12}.
}
\]

Asymmetric inputs are rejected.

---

## 26. Weak-field point-mass cross-check

The phase/lensing machinery includes the standard weak-field expression

\[
\boxed{
|\alpha|
=
\frac{4GM}{bc^2}.
}
\]

The local test suite verifies a numerical instance exactly.

This provides an internal cross-check of the lensing calculation path.

---

## 27. Orbit–epicycle phase-curvature bridge

For orbital angular-frequency square \(\Omega^2(r)\), the epicyclic frequency is

\[
\boxed{
\kappa^2
=
4\Omega^2
+
r\frac{d\Omega^2}{dr}.
}
\]

The radial scalar gradient is

\[
\boxed{
\Phi'(r)
=
r\Omega^2.
}
\]

The second derivative is

\[
\boxed{
\Phi''
=
\kappa^2-3\Omega^2.
}
\]

The radial Hessian eigenvalues are represented as

\[
\boxed{
\left(
\kappa^2-3\Omega^2,
\Omega^2,
\Omega^2
\right).
}
\]

---

## 28. Power-law curvature signatures

For

\[
\Omega^2\propto r^{-q},
\]

one has

\[
\kappa^2=(4-q)\Omega^2.
\]

The repository regression suite checks three reference signatures:

\[
q=3
\Rightarrow
(-2,1,1)\Omega^2,
\]

\[
q=2
\Rightarrow
(-1,1,1)\Omega^2,
\]

\[
q=0
\Rightarrow
(1,1,1)\Omega^2.
\]

These are implemented as exact numerical identities.

---

## 29. Transverse phase geometry

For impact parameter \(b\) and radius \(r\),

\[
\boxed{
\nabla_\perp\Phi
=
b\Omega^2.
}
\]

The transverse curvature implemented by the repository is

\[
\boxed{
\Phi_{\perp\perp}
=
\beta^2\kappa^2
+
(1-4\beta^2)\Omega^2,
\qquad
\beta=\frac br.
}
\]

The implementation fails closed if \(|b|>r\).

---

## 30. Montgomery–Dyson phase spectroscopy

The phase-spectroscopy module separates spatial phase-screen geometry from a declared spectral/eigenphase sequence.

For ordered distinct spectral coordinates \(x_j\), mean-spacing unfolding is

\[
u_j
=
\frac{x_j-x_0}{\langle\Delta x\rangle}.
\]

Phase coordinates are

\[
\boxed{
\Phi_j=2\pi u_j.
}
\]

For Riemann-zero ordinates \(\gamma\), the smooth counting coordinate used is

\[
\boxed{
\bar N(\gamma)
=
\frac{\gamma}{2\pi}
\ln\frac{\gamma}{2\pi}
-
\frac{\gamma}{2\pi}
+
\frac78.
}
\]

The corresponding phase coordinate is

\[
\Phi_\gamma
=
2\pi\bar N(\gamma).
\]

---

## 31. Forced pair law

The repository implements the phase-coordinate pair law

\[
\boxed{
R_2(\Delta\Phi)
=
1-
\operatorname{sinc}^2
\left(
\frac{\Delta\Phi}{2\pi}
\right).
}
\]

At zero separation,

\[
R_2(0)=0,
\]

while at one full phase turn,

\[
R_2(2\pi)=1.
\]

The regression suite verifies both values.

---

## 32. Spectral form factor

For phase coordinates \(\Phi_j\), the raw coherence is

\[
\boxed{
K(\tau)
=
\left|
\frac1N
\sum_{j=1}^N
e^{i\tau\Phi_j}
\right|^2.
}
\]

The normalized finite pair-power form is

\[
\boxed{
S_N(\tau)
=
N K(\tau).
}
\]

The forced microscopic target used in the module is

\[
\boxed{
S(\tau)=\min(|\tau|,1).
}
\]

Global phase-shift invariance is directly tested.

---

## 33. Prime-power carriers

The arithmetic diagnostic enumerates prime powers

\[
q=p^m
\]

up to a declared cutoff.

Each carrier has angular coordinate

\[
\boxed{
\omega_{p,m}
=
m\ln p
=
\ln(p^m),
}
\]

with weight

\[
\boxed{
w_{p,m}
=
\frac{\ln p}{\sqrt{p^m}}.
}
\]

The phase signal is

\[
\boxed{
S(t)
=
-\frac1\pi
\sum_{p^m\le C}
w_{p,m}
e^{-\frac12(\sigma\omega_{p,m})^2}
\cos(t\omega_{p,m}+\varphi_{p,m}).
}
\]

The module includes phase scrambling as a reverse control.

---

## 34. Historical Euclidean tetrahedron control

The repository retains an older six-edge operator tetrahedron as a negative geometric control.

Its exact triangle defect is

\[
\boxed{
\frac1{441}>0,
}
\]

and its Gram determinant is

\[
\boxed{
-\frac{468852409}{90812685325761}<0.
}
\]

Therefore the historical six-edge Euclidean realization fails its own Euclidean gate.

The exact rational values are regression-tested.

This is a useful example of the repository preserving a rejected geometric realization while retaining the broader phase/relational framework.

---

## 35. GREMLIN source-binding crosswalk

The GREMLIN audit gives two explicit routes into flavour space.

### Route A — 36D pullback

\[
H_{\rm QHTRI}\in\mathrm{Herm}(36)
\rightarrow
W^\dagger H_{\rm QHTRI}W
\rightarrow
u(3)
\rightarrow
\text{flavour Hamiltonian}.
\]

### Route B — relational edge assembly

\[
\text{relation source}
\rightarrow
\text{holonomy }\tau
\rightarrow
J_{ij}
\rightarrow
H_{\rm edge}.
\]

Both routes terminate in Hermitian \(3\times3\) operators and can therefore be compared after removal of the common identity component.

The closed edge-cycle phase supplies the rephasing-invariant phase coordinate of Route B.

---

## 36. QHTRI application-specific binding ledger

The repository names several specific application bindings.

### HνQ

The QHTRI oscillator/holonomy state is bound to measurable neutrino phase/flavour transport.

### Hfocus

The QHTRI phase/flavour operator is spatially programmed into a useful focusing response.

### Hg

The QHTRI relation is promoted from an effective propagation/operator description into a spacetime-metric response.

### HZPE

The relevant oscillator-correlation sector is identified with a zero-point/vacuum structure.

### HEB

An EB-condensate observable set supplies the typed relational-state/source map for the orbital information-potential bridge.

These labels belong to those specific bindings. They are separate from the classification of QHTRI itself as an analog computational substrate.

---

## 37. Fail-closed numerical design

The Python implementation consistently rejects malformed state.

Examples include:

- non-finite oscillator inputs;
- zero total oscillator amplitude;
- non-monotone spatial coordinates;
- non-Hermitian Hamiltonians;
- non-unitary mixing matrices;
- invalid probability vectors;
- non-isometric \(36\times3\) embeddings;
- open/invalid geometry inputs;
- nonsymmetric lensing Hessians;
- invalid orbital radii or \(|b|>r\).

The result is a numerical reference surface in which the intended mathematical domain is explicitly checked.

---

## 38. Independent local validation manifest

The following local files were checked against their Git blob SHAs before execution:

- \`pyproject.toml\`;
- all 12 Python package files under \`src/qhtri_phase_optics/\`;
- all 11 test files under \`tests/\`.

Result:

\[
\boxed{
24/24\ \text{blob identities matched}.
}
\]

The byte-exact suite then produced:

\[
\boxed{
65\ \text{passed},\quad
0\ \text{failed}.
}
\]

The validation covers:

- analog oscillator coherence;
- phase slope and curvature;
- PMNS/unitary flavour evolution;
- scalar versus traceless controls;
- Berry holonomy;
- Euler–Berry closure;
- \(36D\to u(3)\) pullback;
- SU(3) reconstruction;
- basis covariance;
- oriented Hermitian exchange;
- flavour-cycle rephasing invariance;
- information curvature and potential;
- potential-to-phase mapping;
- Hamilton–Jacobi mechanics;
- focusing, Jacobian, caustic and shear;
- weak-field lensing cross-check;
- orbit/epicycle curvature;
- exact historical geometry negative control;
- Montgomery–Dyson phase spectroscopy;
- prime-power carrier and phase-scramble controls.

---

## 39. Repository dependency graph

The effective internal dependency graph is

\[
\boxed{
\begin{aligned}
&\text{analog oscillator state}\\
&\downarrow\\
&\text{36D phase state}\\
&\downarrow\\
&\text{Berry / Euler–Berry holonomy}\\
&\downarrow\\
&\begin{cases}
36D\to u(3)\text{ pullback},\\
\text{oriented edge operator}
\end{cases}\\
&\downarrow\\
&\text{Hermitian flavour transport}\\
&\downarrow\\
&\text{phase-gradient / curvature mechanics}\\
&\downarrow\\
&\text{phase optics / spectroscopy}.
\end{aligned}
}
\]

The information-potential path intersects this graph at the phase-mechanics layer:

\[
(p,\pi,A_{\rm rel})
\rightarrow
\Xi_I
\rightarrow
U_I
\rightarrow
\Phi.
\]

---

## 40. Relation to OSCYL8 / GREMLIN

Within the broader OSCYL8 architecture, QHTRI provides an analog computational carrier for phase-native state and dynamics.

GREMLIN contributes:

- source binding;
- relation routing;
- provenance;
- operator composition;
- phase/geometry state management;
- cross-route comparison;
- application-level orchestration.

The present repository gives GREMLIN a concrete numerical QHTRI application interface for neutrino/flavour transport and phase optics.

Thus the stack can be summarized as

\[
\boxed{
\text{OSCYL8}
\supset
\text{GREMLIN}
\leftrightarrow
\text{QHTRI analog substrate}
\rightarrow
\text{application operators}.
}
\]

---

## 41. Canonical repository references

The monograph is grounded directly in:

- \`README.md\`;
- \`THEORY.md\`;
- \`CLAIMS.md\`;
- \`ROADMAP.md\`;
- \`PROVENANCE.md\`;
- \`docs/GREMLIN_SOURCE_BINDING_AUDIT.md\`;
- \`docs/INFORMATIONAL_PHASE_OPTICS.md\`;
- \`docs/PHASE_MECHANICS_GREMLIN_ORBITAL_EB_BRIDGE.md\`;
- \`docs/T36_TO_U3_PULLBACK.md\`;
- \`docs/ORBIT_EPICYCLE_PHASE_CURVATURE_BRIDGE_V0_1.md\`;
- \`docs/MONTGOMERY_DYSON_PHASE_SPECTROSCOPY_V0_1.md\`;
- \`src/qhtri_phase_optics/*.py\`;
- \`tests/*.py\`.

---

## 42. Conclusion

The audited repository implements an end-to-end phase-native mathematical and computational chain from analog QHTRI oscillator state to 36D phase geometry, holonomy, flavour-space operators, path-ordered propagation, informational potential mechanics, phase optics and spectral diagnostics.

Its principal structural interfaces are

\[
\boxed{
\mathbb C^{36}
\rightarrow
u(3)
\rightarrow
\mathrm{Herm}(3)
\rightarrow
U(3)\text{ transport}
}
\]

and

\[
\boxed{
\Xi_I
\rightarrow
U_I
\rightarrow
\Phi
\rightarrow
\nabla\Phi
\rightarrow
\nabla^2\Phi
\rightarrow
\text{optical geometry}.
}
\]

The independent exact-head replay confirms the executable repository state with 24/24 byte-identical package/test blobs and 65/65 passing tests.

QHTRI remains the fully analog computational substrate; the repository then types and tests each downstream physical or application-specific binding separately rather than conflating the status of a particular interface with the nature of QHTRI itself.
