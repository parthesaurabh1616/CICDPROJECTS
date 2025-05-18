import os
from analyzer import analyze_file

def test_analysis_output(capsys):
    test_file = 'sample.txt'
    analyze_file(test_file)
    captured = capsys.readouterr()
    assert "Lines: 5" in captured.out
    assert "Words:" in captured.out
    assert "Characters:" in captured.out