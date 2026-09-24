/// [GOAL] ::: Create A Process by using C to Linux Systems : currently only process create understanding about.

#include <stdio.h>
/// For System Calls
#include <unistd.h>

#include <sys/wait.h>

int main() {
    typedef pid_t b;
    int pid = fork(); /// int given instead og pid_t because, int as pid_t using `type_def`

    if (pid < 0){
        printf("\n\033[91mProcess Creation Failed!\n");
    }   else if (pid == 0) {
        printf("\033[94mChild Process Creation Passed \033[93m:)\n, \033[95mPID = %d\n\033[0m", getpid());
    } else {
        printf("Parent Process, PID = %d, Child PID = %d\n", getpid(), pid);
        wait(NULL);
    }
    return 0;

}