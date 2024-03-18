I have to:
- [/] Find all logbooks in the buffer
- [ ] Determin whether "CLOCK:" has been calculated before
    - If they have "=>" in the line, then it has already been calculated
        - When do we want to update it?
    - [ ] Store calculated status, regardless whether we want to update it or not
- [ ] calculate elapsed time, if needed
- [ ] append `CLOCK:` entry with updated time, if it's been calculated
- [ ] write/update buffer with the updated :LOGBOOK:s
