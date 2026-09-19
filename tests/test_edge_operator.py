import numpy as np

from qhtri_phase_optics.edge_operator import (
    assemble_oriented_flavour_exchange,
    flavour_cycle_phase,
    rephase_flavour_operator,
    route_mismatch,
    traceless_part,
)


def test_oriented_edge_assembly_is_hermitian():
    H = assemble_oriented_flavour_exchange(1 + 2j, 0.3 - 0.7j, -0.2 + 0.4j)
    assert np.allclose(H, H.conj().T, atol=1e-13)


def test_cycle_phase_is_invariant_under_local_flavour_rephasing():
    H = assemble_oriented_flavour_exchange(1 + 2j, 0.3 - 0.7j, -0.2 + 0.4j)
    gamma0 = flavour_cycle_phase(H)
    Hr = rephase_flavour_operator(H, np.array([0.2, -0.7, 1.1]))
    gamma1 = flavour_cycle_phase(Hr)
    assert gamma0 is not None and gamma1 is not None
    assert np.isclose(np.exp(1j * gamma0), np.exp(1j * gamma1), atol=1e-12)


def test_identity_shift_does_not_change_traceless_edge_route():
    H = assemble_oriented_flavour_exchange(0.1j, 0.2 + 0.1j, -0.3j)
    shifted = H + 4.2 * np.eye(3)
    assert np.allclose(traceless_part(H), traceless_part(shifted), atol=1e-12)


def test_route_mismatch_ignores_common_identity_when_requested():
    H = assemble_oriented_flavour_exchange(0.4 + 0.2j, -0.1j, 0.3 - 0.5j)
    assert route_mismatch(H + 2.0 * np.eye(3), H, remove_identity=True) < 1e-12
    assert route_mismatch(H + 2.0 * np.eye(3), H, remove_identity=False) > 1.0
