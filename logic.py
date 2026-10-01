import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

def late_rate(zone, time_block, promise):
    if zone != 'all' and time_block != 'all':
        times = delivery_times(zone, time_block, promise)
    elif zone == 'all' and time_block != 'all':
        times = np.concatenate([delivery_times(z, time_block, promise) for z in ZONES])
    elif zone != 'all' and time_block == 'all':
        times = np.concatenate([delivery_times(zone, tb, promise) for tb in TIME_BLOCKS])
    else:  # both 'all'
        times = np.concatenate([delivery_times(z, tb, promise) for z in ZONES for tb in TIME_BLOCKS])

    late_count = np.sum(times > promise)
    percent_late = late_count / len(times) * 100
    return percent_late

def avg_delivery_time(zone, time_block, promise):
    if zone != 'all' and time_block != 'all':
        times = delivery_times(zone, time_block, promise)
    elif zone == 'all' and time_block != 'all':
        times = np.concatenate([delivery_times(z, time_block, promise) for z in ZONES])
    elif zone != 'all' and time_block == 'all':
        times = np.concatenate([delivery_times(zone, tb, promise) for tb in TIME_BLOCKS])
    else:  # both 'all'
        times = np.concatenate([delivery_times(z, tb, promise) for z in ZONES for tb in TIME_BLOCKS])

    avg_time = np.mean(times)
    return avg_time

def cost_per_late_order(costs):
  refund = costs['refund']
  churn = costs['churn_orders']
  margin = costs['margin']
  total_cost = refund + (churn * margin)
  return total_cost

def best_promise(zone, time_block, promises, costs):
    best = None
    best_profit = None

    for promise in promises:
        times = delivery_times(zone, time_block, promise)
        num_orders = len(times)
        num_late = np.sum(times > promise)

        margin = costs['margin']
        cost_per_late = cost_per_late_order(costs)

        net_profit = (num_orders*margin)-(num_late*cost_per_late)

        if best_profit is None or net_profit > best_profit:
            best = promise
            best_profit = net_profit

    return best, best_profit