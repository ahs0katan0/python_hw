text = "X-DSPAM-Confidence:    0.8475";
numfind = text.find(':')
remaintext = text[numfind+1:]
numonly = float(remaintext)
print numonly
# Dummy comment