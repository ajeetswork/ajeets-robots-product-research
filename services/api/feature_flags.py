def build_feature_flag_response(flags):
    ordered_flags = sorted(
        flags,
        key=lambda flag: (flag["rollout_index"], flag["flag_key"]),
    )

    return {
        "flags": [
            {
                "flag_key": flag["flag_key"],
                "enabled": flag["enabled"],
                "rollout_index": flag["rollout_index"],
            }
            for flag in ordered_flags
        ]
    }
