# Test Infrastructure

This directory contains standalone unit test suites for the project. Tests are run using `pytest`.

## Test Suites

| File | Target Module | Scope |
|------|---------------|-------|
| `test_packet_parser.py` | Shared | 28-byte packet parsing, CRC16 verification, error recovery |
| `test_angle_calculator.py` | Module 3 | Vector dot product angle math, low-pass filter, interpolation |
| `test_analysis_engine.py` | Module 2 | Sliding window RMSE/MAE metrics, Bland-Altman statistics |

## Running Tests

```bash
# Run all test suites
pytest tests/ -v

# Run a specific test suite
pytest tests/test_packet_parser.py -v

# Run with test coverage reporting
pytest tests/ --cov=shared --cov=module2_interface_rmse --cov=module3_mediapipe_simulation
```

## Testing Standards & Conventions

- Every new calculation or utility function must include both positive and negative/boundary test cases.
- Mark tests requiring physical hardware with `@pytest.mark.hardware`.
- Mark tests requiring an optical camera or video capture device with `@pytest.mark.camera`.
- Validate angle computation against known trigonometric vectors (0°, 45°, 90°, 180°).
