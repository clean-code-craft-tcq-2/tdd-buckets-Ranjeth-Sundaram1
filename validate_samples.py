def PrintSampleDetailsIntoConsole(samples, count):
    messagetoprint = (f"{samples[0]}-{samples[-1]}, {count}")
    print(messagetoprint)
    return(messagetoprint)

def SplitSamplesInToRanges(input_samples:list):
    in_range_samples = []
    sample_collections = []
    for sample in input_samples:
        is_Sample_in_Range = IsSampleInRange(sample=sample, in_range_samples= in_range_samples)
        if is_Sample_in_Range:
            in_range_samples.append(sample)
            if sample == input_samples[-1]:
                sample_collections.append(in_range_samples)
        else:
            sample_collections.append(in_range_samples)
            in_range_samples = []
    return sample_collections

def validateSamplesInAllRange(input_samples:list):
    sample_collections = SplitSamplesInToRanges(input_samples=input_samples)
    validation_report = []
    for one_collection in sample_collections:
        validation_report.append(CountAndPrintSamplesinOneRange(one_collection=one_collection))
    return validation_report

def CountAndPrintSamplesinOneRange(one_collection=None):
    messagefromConsole = PrintSampleDetailsIntoConsole(one_collection, len(one_collection))
    return (len(one_collection), messagefromConsole)

def IsSampleHasContinuity(sample, in_range_samples):
    if in_range_samples != []:
        if sample == int(in_range_samples[-1])+1:
            return True
        return False
    return True

def IsSampleInRange(sample, in_range_samples):
    if sample not in in_range_samples and IsSampleHasContinuity(sample, in_range_samples):
        return True
    return False

def RemoveOccuranceOneSample(sample_collections):
    filtered_samples = []
    for samples in sample_collections:
        if len(samples) != 1:
            filtered_samples.append(samples)
        pass
    return filtered_samples
