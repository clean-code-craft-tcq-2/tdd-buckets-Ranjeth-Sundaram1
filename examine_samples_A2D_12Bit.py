def IgnoreInvalidSamples(input_samples : list):
    if input_samples != []:
        samples_to_examine = [sample for sample in input_samples if sample <= 4094]
        return samples_to_examine
    return input_samples
