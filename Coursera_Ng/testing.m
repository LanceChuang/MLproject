 % fminunc optimization algorithm is built-in function in Octave.
 % along with the "optimset()" function that creates an object containing the options 
 % we want to send to "fminunc()"


options = optimset('GradObj','on','MaxIter',100);
initialTheta = zeros(2,1);
[optTheta,functionVal,exitFlag] = fminunc(@costFunction,initialTheta,options);
fprintf('optTheta is %d\n',optTheta);
fprintf('functionVal is %d\n',functionVal);
%fprintf('exitFlag is %d',exitFlag);
