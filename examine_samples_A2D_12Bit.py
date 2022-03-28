import examine_samples

def IgnoreInvalidSamples(input_samples : list):
    if input_samples != []:
        samples_to_examine = [sample for sample in input_samples if sample <= 4094]
        return samples_to_examine
    return input_samples

def convertA2D_12BIntoAmps(input_samples: list):
    samples_to_examine = IgnoreInvalidSamples(input_samples)
    samples_to_examine = [round(sample*10/4094) for sample in samples_to_examine]
    return samples_to_examine

def ExamineSamplesFrom_A2D(input_samples: list):
    samples_to_examine = convertA2D_12BIntoAmps(input_samples)
    found_sample_ranges = examine_samples.IdentifyRangesofSamples(samples_to_examine)
    return found_sample_ranges
