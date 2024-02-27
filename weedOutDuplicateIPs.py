import re

def remove_duplicate_ips_within_blocks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []  # Store the processed file content
    block_lines = []  # Temporarily store lines within a block
    ip_occurrences = {}  # Track occurrences of IP addresses within a block
    block_depth = 0  # Track the depth of nested blocks

    # Enhanced regular expression to accurately match IPv4, IPv6, and CIDR notation
    ip_pattern = re.compile(r"^\s*((?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?|\[?[A-Fa-f0-9:]+\]?)(/\d{1,2})?\s")

    def process_block():
        for line in block_lines:
            match = ip_pattern.match(line)
            if match:
                # Include both IP address and CIDR notation as the unique key
                ip_key = match.group(0).strip()
                if ip_occurrences[ip_key] > 1:
                    ip_occurrences[ip_key] -= 1
                    continue  # Skip earlier occurrences
            new_lines.append(line)

    for line in lines:
        if '{' in line:
            if block_depth == 0:
                block_lines = []
                ip_occurrences = {}
            block_depth += 1
        elif '}' in line:
            block_depth -= 1
            if block_depth == 0:  # End of a block
                process_block()
                new_lines.append(line)
                continue

        if block_depth > 0:
            block_lines.append(line)
            match = ip_pattern.match(line)
            if match:
                # Include both IP address and CIDR notation as the unique key
                ip_key = match.group(0).strip()
                ip_occurrences[ip_key] = ip_occurrences.get(ip_key, 0) + 1
        else:
            new_lines.append(line)

    # Write the processed content back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    file_path = '/etc/nginx/conf.d/globalblacklist.conf'  # Adjust the file path as needed
    remove_duplicate_ips_within_blocks(file_path)



