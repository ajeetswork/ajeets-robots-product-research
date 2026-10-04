#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${PR_NUMBER:-}" ]]; then
  echo "PR_NUMBER is required" >&2
  exit 1
fi

gh api   --method POST   -H "Accept: application/vnd.github+json"   "/repos/${GITHUB_REPOSITORY}/issues/${PR_NUMBER}/comments"   -f body="Research preview completed successfully for commit ${GITHUB_SHA}."
