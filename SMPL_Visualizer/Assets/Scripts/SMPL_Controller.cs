using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class SMPL_Controller : MonoBehaviour
{
    Vector3[,] joint_motions;
    int frame_counter = 0;
    // int angle = 90;

    Dictionary<string, int> joint_indices = new Dictionary<string, int>
    {
        ["hip"] = 0,
        ["upperleg_l"] = 1,
        ["upperleg_r"] = 2,
        ["spine_01"] = 3,
        ["lowerleg_l"] = 4,
        ["lowerleg_r"] = 5,
        ["spine_02"] = 6,
        ["foot_l"] = 7,
        ["foot_r"] = 8,
        ["spine_03"] = 9,
        ["ball_l"] = 10,
        ["ball_r"] = 11,
        ["neck"] = 12,
        ["shoulder_l"] = 13,
        ["shoulder_r"] = 14,
        ["head"] = 15,
        ["upperarm_l"] = 16,
        ["upperarm_r"] = 17,
        ["lowerarm_l"] = 18,
        ["lowerarm_r"] = 19,
        ["hand_l"] = 20,
        ["hand_r"] = 21
    };

    // Start is called before the first frame update
    void Start()
    {
        string fileData = System.IO.File.ReadAllText("Assets/Data/out.csv");
        string[] lines = fileData.Split("\n");
        joint_motions = new Vector3[lines.Length, lines[0].Split(",").Length / 3];

        for (int i = 0; i < lines.Length; i++){
            string[] frame_joints = lines[i].Split(",");
            for (int j = 0; j < frame_joints.Length; j += 3){
                Vector3 joint = new Vector3(float.Parse(frame_joints[j]), float.Parse(frame_joints[j + 1]), float.Parse(frame_joints[j + 2]));
                joint_motions[i, j / 3] = joint;
            }
        }

    }
    
    // Update is called once per frame
    void Update()
    {
        foreach (Transform t in gameObject.GetComponentsInChildren<Transform>()){
            if (joint_indices.ContainsKey(t.name)){
                t.rotation = Quaternion.Euler(joint_motions[frame_counter, joint_indices[t.name]]);
            }
        }

        if (frame_counter < joint_motions.GetLength(0) - 1){
            frame_counter += 1;
        } else {
            frame_counter = 0;
            // angle += 45;
        }
    }
}
