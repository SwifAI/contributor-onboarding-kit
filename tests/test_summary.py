from contributor_onboarding_kit import format_summary


def test_format_summary_includes_name_and_notes() -> None:
    assert format_summary("Ava", ["read docs"]) == "Contributor Ava: read docs"
