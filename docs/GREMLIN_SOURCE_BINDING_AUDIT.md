# GREMLIN Source-Binding Audit — QHTRI / Three-Flavour Interface

Status: REPRESENTATION_AND_OPERATOR_ROUTES_NARROWED / PHYSICAL_EDGE_AND_SECTOR_BINDINGS_OPEN

Date: 2026-09-19

## 1. Result

The QHTRI-to-neutrino problem no longer needs to be represented as one arbitrary map.

Two independent mathematical routes now exist.

### Route A — carrier pullback

    H_QHTRI in Herm(36)
      -> Pi_W(H_Q)=W^dagger H_Q W
      -> u(3)
      -> v0, xi_1,...,xi_8

This route is implemented in pullback.py. Its remaining physical debt is the provenance of W / Pi_36_to_nu.

### Route B — provenance-bearing oriented edge assembly

GREMLIN v0.9 -> v1.4 -> v1.5 already supplies the model chain:

    bound connection path
      -> holonomy tau
      -> QHTRI lag receipt
      -> oriented complex exchange J
      -> selected flavour edge
      -> Hermitian 3x3 neutrino Hamiltonian

For three oriented couplings define J_e_mu, J_mu_tau and J_tau_e and assemble

    H_QF =
    [ d_e          J_e_mu         conj(J_tau_e) ]
    [ conj(J_e_mu) d_mu           J_mu_tau       ]
    [ J_tau_e      conj(J_mu_tau) d_tau          ].

The loop phase Gamma_3 = arg(H_e_mu H_mu_tau H_tau_e) is invariant under local flavour-basis rephasing.
This route does not require assigning semantic meaning to individual T36 coordinate indices.

Its remaining physical debt is the map from a QHTRI relation/loop to a physical flavour edge and, for diagonal terms, the source of each flavour-dependent diagonal channel.

## 2. GREMLIN neutrino lineage recovered

Relevant existing GREMLIN surfaces:

- GREMLIN_THREE_FLAVOR_NEUTRINO_HAMILTONIAN_V1_5
- GREMLIN_BELZEBUB_FLAVOR_INFORMATION_AUDIT_V1_6
- GREMLIN_INTENTION_FLAVOR_BRIDGE_V1_7
- GREMLIN_INTENTION_MASS_FLAVOR_FACTORIZATION_V1_8
- GREMLIN_J_IDENTIFIABILITY_NO_GO_V1_9
- GREMLIN_J_INVARIANT_REDUCTION_AUDIT_V2_0
- GREMLIN_COMPLEX_OVERLAP_FRAME_BRIDGE_V2_3
- GREMLIN_NEUTRINO_CANON_LEDGER_V2_4

The v1.7-v2.3 sequence progressively reduces a hidden cross-space identification to explicit source-binding debt. v2.3 removes arbitrary U(3) freedom conditionally once a labelled orthonormal neutrino frame is source-bound.

## 3. TIR v12 representation status

TIR v12 independently closes V_F ~= C^3, SU(3)_F, dim su(3)_F = 8, and the mixing incidence count 3 x 8 = 24.
It records 24 = |S4| as an independent finite-symmetry crosscheck, not as a physical identification.

The 2026-09-19 TIR-IDT crosswalk closes an ordered C3 <-> family C3 label intertwiner while explicitly retaining the physical temporal/flavour sector identification as OPEN.

RFC-S12 further shows that a regular tetrahedral congruence leaves only a finite role coordinate: S4 before orientation and A4 after orientation. A unique physical role map still requires independently sourced role signatures.

Therefore an abstract/representation-level match must not be promoted into a physical neutrino coupling without an independent sector-binding receipt.

## 4. T36 firewall

No canonical source was found for a decomposition 36 = 24 + 12 that identifies T36 coordinate blocks with flavour-mixing channels plus a physical residual sector.

Existing PhaseNav/NOEMA sources explicitly distinguish intrinsic states from their 36D routing/holonomy realization. Hash-derived semantic T36 addresses are computational addresses and are not physical flavour embeddings.

Accordingly this project does not assign flavour semantics directly to T36 coordinate numbers.

## 5. Historical v11 operator-tetrahedron firewall

The historical Metatime operator tetrahedron used the six edge assignments:

    |I-M|        = 2/7
    |I-A_mu|     = 2/9
    |I-A_tau|    = 1/7
    |M-A_mu|     = 2/49
    |M-A_tau|    = 20/49
    |A_mu-A_tau| = 18/49

As ordinary Euclidean distances these fail exactly.

On the face (I,A_mu,A_tau):

    18/49 - (2/9 + 1/7) = 1/441 > 0.

Thus the triangle inequality is violated.

The Gram matrix reconstructed from the same six distances has exact determinant

    -468852409 / 90812685325761 < 0,

so it is not positive semidefinite.

This is a deterministic FAIL of the ordinary Euclidean-tetrahedron interpretation of that historical edge set. It is not evidence that 1/441 has a physical meaning.

TIR v12 independently quarantines the old operator-tetrahedron dihedral shortcut and the old volume/kappa-cubed binding as noncanonical geometry sources. The canonical v12 tetrahedral theorem uses the regular Gram class instead.

## 6. Current minimal physical debts

    A. labelled neutrino/family representation -> physical flavour sector
    B. QHTRI relation/loop -> physical flavour edge (or full Pi_36_to_nu)
    C. coupling magnitude/units calibration
    D. independent physical data

Everything downstream of a supplied Hermitian 3x3 operator is already standard or implemented: SU(3) decomposition, path-ordered propagation, null controls, and phase-optics targets.

## 7. Cross-route falsification gate

If both Route A and Route B receive independent provenance-bearing physical bindings, compare their traceless operators:

    Delta_route =
      || traceless(Pi_W(H_Q)) - traceless(H_QF) ||.

Agreement is a nontrivial consistency test. Disagreement falsifies at least one binding/adapter assumption; it must not be averaged away.
