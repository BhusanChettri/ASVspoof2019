function [consecutiveZeros] = count_consecutive_zeros(samples)

% Count the first consecutive block of zeros from an array of audio sample
% and return the count

consecutiveZeros=0;

%fprintf('Total samples = %d ', length(samples));

for i=1:length(samples)
    if samples(i)==0        
        consecutiveZeros = consecutiveZeros+1;
    else
        break;
    end 
end

end

