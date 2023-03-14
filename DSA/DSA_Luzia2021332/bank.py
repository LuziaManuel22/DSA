wall-clock = 0; teller = ‘free’
// initialize wall-clock = 0 in min;
 bank is open; Teller is Free

bank-closing-time = 600
// bank to close at 600 min

Initialize queue Q as empty

Schedule cust-arr-event (cust-id = 1, event-time = wall-clock + IAT*random())

Schedule cust-dep-event (cust-id = ‘None’, event-time = ꚙ)
// no customer being serviced

Initialize list wait-times =[]
// to be used to generate stats on waiting times

repeat

Compute next-event, cust-id, event-time
// compare time of cust-arr-event, cust-dep-event

wall-clock = event-time

cust-id = cust-id

If next-event = cust-arr-event and wall-clock < 600 then {

enqueue(Q, (cust-id, wall-clock))
// record cust-id & her time of arrival

if teller = ‘free’ then {

Schedule cust-dep-event (cust-id = cust-id, event-time = wall-clock + ST*random())

teller = ‘busy’

}

Schedule cust-arr-event (cust-id = cust-id + 1, event-time = wall-clock + IAT*random())

}

If next-event = cust-dep-event then {

(cust-id, arr-time) = dequeue(Q)

append(cust-id, arr-time, wall-clock)

if queue Q is not empty then {

cust-id = front(Q).cust-id

Schedule cust-dep-event (cust-id = cust-id, event-time = wall-clock + ST*random())

teller = ‘busy’

}

}

until wall-clock >= closing-time and queue Q is empty